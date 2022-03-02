from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from database import get_session
from users.models import User, UserCreate

def create_user(user: UserCreate, db: Session = Depends(get_session)):
    user_to_db = User.from_orm(user)
    db.add(user_to_db)
    db.commit()
    db.refresh(user_to_db)
    return user_to_db