from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional

from schemas.Boops import Boop

class ImageBase(BaseModel):
    url: str
    
class Image(BaseModel):
    id: int
    url: str
    user_id: int
    dog_id: int
    boops: Optional[list[Boop]] = None
    
    class Config: 
        orm_mode=True
        
class ImageOut(BaseModel):
    id: int
    
    class Config:
        orm_mode=True