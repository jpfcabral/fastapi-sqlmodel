from fastapi import Depends, HTTPException, status
from sqlmodel import Session
import bcrypt
from database import get_session
from users.models import User, UserCreate

def create_user(user: UserCreate, db: Session = Depends(get_session)):
    hashed_password = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt())
    user_to_db = User(**user.dict(), hashed_password=hashed_password)
    db.add(user_to_db)
    db.commit()
    db.refresh(user_to_db)
    return user_to_db