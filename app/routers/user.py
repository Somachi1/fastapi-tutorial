from fastapi import Depends, FastAPI, HTTPException, Response, status, APIRouter
from typing import List
from sqlalchemy.orm import Session
from .. import models, schema, utils
from ..database import get_db


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schema.UserResponse])
def get_user(db: Session=Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.UserResponse)
def create_user(user: schema.CreateUser, db: Session=Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)              
    db.commit()       
    db.refresh(new_user)
    
    return new_user

 
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schema.UserResponse)
def get_user(id: int, db: Session=Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id:{id} does not exist")
    return user