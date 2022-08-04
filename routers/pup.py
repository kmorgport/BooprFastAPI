from fastapi import Depends, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import  List, Optional
from models.Dog import Dog
from database.oauth2 import get_current_user

from schemas import Dogs, Breeds
from database import database
# from models import Dog as model
from models.Dog import Dog
from models.Breed import Breed
from models.Boop import Boop
from models.Image import Image
from models.Dog_Breeds import Dog_Breeds


router = APIRouter(
    prefix="/dogs",
    tags=["Dogs"]
)

@router.get("/", response_model=List[Dogs.DogOut])
async def get_dogs(db: Session = Depends(database.get_db), search: Optional[str]=""):
    dogs = db.query(Dog).filter(Dog.name.contains(search)).all()
    
    for dog in dogs:
        breeds = db.query(Breed).filter(Dog_Breeds.breed_id == Breed.id, Dog_Breeds.dog_id == Dog.id).filter(Dog.id == dog.id).all()
        dog.breeds = breeds
            
    return dogs

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Dogs.DogOut)
async def post_dog(dog: Dogs.DogCreate, db: Session = Depends(database.get_db), current_user: int = Depends(get_current_user)):
    print(dog)
    new_dog = Dog(owner_id=current_user.id, name=dog.name, sex=dog.sex, bio=dog.bio, age=dog.age )
    db.add(new_dog)
    db.commit()
    db.refresh(new_dog)
    for breed in dog.breeds:
        new_join_table_entry = Dog_Breeds(dog_id=new_dog.id, breed_id=breed.id)
        db.add(new_join_table_entry)
        db.commit()
        db.refresh(new_join_table_entry)
    
    dog_query = db.query(Dog).filter(Dog.id == new_dog.id).first()
    
    return dog_query
    
    

@router.get("/{id}", response_model=Dogs.DogOut)
async def get_pup(id: int, db: Session = Depends(database.get_db)):
    
    dog = db.query(Dog).filter(Dog.id == id).first()
    breeds = breeds = db.query(Breed).filter(Dog_Breeds.breed_id == Breed.id, Dog_Breeds.dog_id == Dog.id).filter(Dog.id == dog.id).all()
    dog.breeds = breeds
    
    if not dog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
        
    return dog

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(database.get_db)):
    
    deleted_pup = db.query(Dog).filter(Dog.id == id)
    
    pup = deleted_pup.first()
    
    if pup == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not authorized to perform requested action")
        
    deleted_pup.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch("/{id}",response_model=Dogs.DogOut)
async def update_post(id: int, updated_dog:Dogs.DogOptional, db: Session = Depends(database.get_db)):
    
    dog_query = db.query(Dog).filter(Dog.id == id)
    dog_check = dog_query.first()
    if dog_check == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dog with id{id} does not exist ")
    
    dog = {
        "name":updated_dog.name,
        "bio": updated_dog.bio,
        "age": updated_dog.age,
        "sex":updated_dog.sex,
    }
    db.query(Dog_Breeds).filter(Dog_Breeds.dog_id == id).delete()
    for breed in updated_dog.breeds:
        new_join_table_entry = Dog_Breeds(dog_id=id, breed_id=breed.id)
        db.add(new_join_table_entry)
        db.commit()
        db.refresh(new_join_table_entry)
    dog_query.update(dog, synchronize_session=False)
    updated_dog = dog_query.first()
    db.commit()
    breeds = breeds = db.query(Breed).filter(Dog_Breeds.breed_id == Breed.id, Dog_Breeds.dog_id == Dog.id).filter(Dog.id == id).all()
    updated_dog.breeds = breeds
    return updated_dog
    