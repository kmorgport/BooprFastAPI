from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional

class DogBase(BaseModel):
    name: str
    bio: str
    sex: bool
    age: int
    
class DogCreate(DogBase):
    pass

class Dog(BaseModel):
    id: int
    created_at: datetime
    owner_id: int
    
    class Config:
        orm_mode=True
        
class DogOut(DogBase):
    id: int
    class Config:
        orm_mode=True
    
    