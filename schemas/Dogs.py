from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import TYPE_CHECKING, List, Optional
    


class DogBase(BaseModel):
    name: str
    bio: str
    sex: bool
    age: int

    class Config:
        orm_mode=True
        allow_population_by_field_name = True
    

class Dog(BaseModel):
    name: str
    sex: bool
    bio: str
    age: int
    
    class Config:
        orm_mode=True
        allow_population_by_field_name = True
        
class DogCreate(DogBase):
    breeds: "list[Breed]"
        
    class Config:
        orm_mode=True
        allow_population_by_field_name = True
        
class DogUpdate(BaseModel):
    name: Optional[str] = None
    sex: Optional[bool] = None
    bio: Optional[str] = None
    age: Optional[int] = None
    # breeds: "Optional[list[Breed]]" = None
    # images: "Optional[list[Image]]" = None
    
    class Config:
        orm_mode=True
        allow_population_by_field_name = True
        
class DogOptional(DogCreate):
    __annotations__ = {k: Optional[v] for k, v in DogCreate.__annotations__.items()}
    
        
class DogOut(DogBase):
    id: int
    name: str
    sex: bool
    bio: str
    age: int
    breeds: "Optional[list[Breed]]" = None
    created_at: datetime
    owner_id: int
    images: "Optional[list[Image]]" = None
    
from Breeds import Breed
from Images import Image
DogOut.update_forward_refs()

from Breeds import Breed
from Images import Image
DogUpdate.update_forward_refs()

from Breeds import Breed
DogCreate.update_forward_refs()

from Breeds import Breed
DogOptional.update_forward_refs()