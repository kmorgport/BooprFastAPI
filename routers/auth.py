from email.policy import HTTP
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import database, utilities, oauth2
from models import User
from schemas import Users, Token

router = APIRouter(
    prefix="/login",
    tags=['Authentication']
)

@router.post("/", response_model=Token.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    user = db.query(User.User).filter(
        User.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    if not utilities.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
        
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    
    return {"access_token":access_token, "token_type": "bearer"}
    