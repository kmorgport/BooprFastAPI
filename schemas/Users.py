from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from schemas.Boops import Boop

import Images


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
    
    class Config:
        orm_mode = True
        
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    dogs: "List[Dog]"
    
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
from Dogs import Dog
UserOut.update_forward_refs()