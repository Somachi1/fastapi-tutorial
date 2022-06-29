from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime 
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str



class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    


class PostCreate(Post):
    pass


class PostResponse(Post):
    created_at: datetime 
    id: int
    user_id: int
    owner: UserResponse
    
    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]= None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
