from typing import List, Optional
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session
from .. import schema, models, oath2
from ..database import get_db
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",
    tags=['Post']
)


# @router.get("/", response_model=List[schema.PostResponse])
@router.get("/")
def get_post(db: Session = Depends(get_db), current_user: int= Depends(oath2.get_current_user), limit: int=10, search: Optional[str]=""):
    
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).all()

    results = db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(models.Votes, models.Votes.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()            

    return results


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.PostResponse)
def create_post(post: schema.PostCreate, db: Session = Depends(get_db), current_user: int= Depends(oath2.get_current_user)):
   
    new_post = models.Post(user_id=current_user.id, **post.dict())
    db.add(new_post)              
    db.commit()       
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schema.PostResponse)
def get_post(id: int, db: Session = Depends(get_db), current_user: int= Depends(oath2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID- {id}, was not found")
    return post
 

@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends((get_db)), current_user: int= Depends(oath2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)       
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID- {id}, was not found")
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}", response_model=schema.PostResponse)
def update_post(id: int, post: schema.Post, db: Session = Depends(get_db), current_user: int= Depends(oath2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID- {id}, was not found")

    if updated_post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")

    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return  updated_post


 

