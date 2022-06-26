from fastapi import Depends, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import  List, Optional

from schemas import Dogs
from database import database
from models import Dog as model

router = APIRouter(
    prefix="/dogs",
    tags=["Dogs"]
)

@router.get("/", response_model=List[Dogs.DogOut])
async def get_dogs(db: Session = Depends(database.get_db), search: Optional[str]=""):
    dogs = db.query(model.Dog).filter(model.Dog.name.contains(search)).all()
    
    return dogs

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Dogs.Dog)
async def post_dog(dog: Dogs.DogCreate, db: Session = Depends(database.get_db)):
    
    new_dog = model.Dog(owner_id=1, **dog.dict())
    db.add(new_dog)
    db.commit()
    db.refresh(new_dog)
    return new_dog