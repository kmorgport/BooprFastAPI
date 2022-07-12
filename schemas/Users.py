from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional
from schemas.Boops import Boop

from schemas.Dogs import Dog
from schemas.Images import Image

class UserBase(BaseModel):
    email: EmailStr
    password: str
    username: str
    
class UserCreate(UserBase):
    pass

class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    username: str
    dogs: Optional[list[Dog]] = None
    images: Optional[list[Image]] = None
    boops: Optional[list[Boop]] = None
    
    class Config:
        orm_mode = True
        
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str