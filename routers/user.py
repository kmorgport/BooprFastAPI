from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas import Users
from database import database, utilities
from models import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Users.UserOut)
async def create_user( user: Users.UserCreate, db: Session = Depends(database.get_db)):
    hashed_password = utilities.hash(user.password)
    user.password = hashed_password
    
    new_user = User.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}')
async def get_user(id: int, db: Session = Depends(database.get_db)):
    return {"message" : f'User No {id}'}


    