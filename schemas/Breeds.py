from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import TYPE_CHECKING, List, Optional

class BreedBase(BaseModel):
    breed: str
    
class BreedCreate(BreedBase):
    pass

class Breed(BaseModel):
    id: int
    breed: str
    
    class Config:
        orm_mode=True
        allow_population_by_field_name = True
        
class BreedOut(Breed):
    dogs: "list[Dog]"
    
from Dogs import Dog
BreedOut.update_forward_refs()
        