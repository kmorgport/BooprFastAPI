from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional

class BreedBase(BaseModel):
    breed: str
    
class BreedCreate(BreedBase):
    pass

class Breed(BaseModel):
    id: int
    breed: str
    
    class Config:
        orm_mode=True
        