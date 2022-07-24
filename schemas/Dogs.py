from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import List, Optional
from schemas.Breeds import Breed

from schemas.Images import Image, ImageBase

class DogBase(BaseModel):
    name: str
    bio: str
    sex: bool
    age: int
    breeds: list[Breed]
    images: Optional[list[Image]] = None
    
class DogCreate(DogBase):
    pass

class Dog(BaseModel):
    id: int
    name: str
    sex: bool
    bio: str
    age: int
    breeds: list[Breed]
    created_at: datetime
    owner_id: int
    images: Optional[list[Image]] = None
    
    class Config:
        orm_mode=True
        
class DogUpdate(BaseModel):
    name: Optional[str]
    sex: Optional[bool]
    bio: Optional[str]
    age: Optional[int]
    breeds: list[Breed]
    images: Optional[list[Image]]
    
    class Config:
        orm_mode=True
        
class DogOut(DogBase):
    id: int
    name: str
    sex: bool
    bio: str
    age: int
    breeds: list[Breed]
    created_at: datetime
    owner_id: int
    images: Optional[list[Image]] = None
    class Config:
        orm_mode=True
    
    