from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional

class BoopBase(BaseModel):
    pass

class Boop(BaseModel):
    id: int
    image_id: int
    user_id: int
    
    class Config:
        orm_mode=True
        
class BoopOut(BaseModel):
    id: int
    
    class Config: 
        orm_mode=True