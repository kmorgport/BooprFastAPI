from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from models.User import User
from models.Dog import Dog
from schemas import Users
from database import database, utilities

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Users.UserOut)
async def create_user( user: Users.UserCreate, db: Session = Depends(database.get_db)):
    hashed_password = utilities.hash(user.password)
    user.password = hashed_password
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}')
async def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(User).filter(User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id:{id} does not exist.")
    
    return user


    