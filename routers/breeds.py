from fastapi import Depends, Response, status, HTTPException, Depends, APIRouter
from requests import delete
from sqlalchemy.orm import Session
from typing import  List, Optional
from models.Dog import Dog

from schemas import Breeds
from database import database, oauth2
# from models import Dog as model

#use models.<Name> syntax so constructor can be properly imported
from models.Dog import Dog
from models.Breed import Breed

router = APIRouter(
    prefix="/breeds",
    tags=["Breeds"]
)

@router.get("/", response_model=List[Breeds.Breed])
async def get_breeds(db: Session = Depends(database.get_db), search: Optional[str]=""):
    breeds = db.query(Breed).filter(Breed.breed.contains(search)).all()
    
    return breeds

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Breeds.Breed)
async def create_breed(breed:Breeds.BreedCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_breed = Breed(**breed.dict())
    db.add(new_breed)
    db.commit()
    db.refresh(new_breed)
    return new_breed

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_breed(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    deleted_breed = db.query(Breed).filter(Breed.id == id)
    print(deleted_breed)
    
    breed = deleted_breed.first()
    
    if breed == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Breed with id: {id} does not exist")
        
    if not current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")
        
    deleted_breed.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)