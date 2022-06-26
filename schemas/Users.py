from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    password: str
    
class UserCreate(UserBase):
    pass

class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
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