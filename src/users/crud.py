import bcrypt
from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select, col
from database import get_session
from users.models import User, UserCreate

def create_user(user: UserCreate, db: Session = Depends(get_session)):
    if read_user(user.username, db=db):
        raise HTTPException(status_code=409, detail='Username or email conflict')
    hashed_password = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt())
    user_to_db = User(**user.dict(), hashed_password=hashed_password)
    db.add(user_to_db)
    db.commit()
    db.refresh(user_to_db)
    return user_to_db

def read_user_by_id(user_id: int, db: Session = Depends(get_session)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User not found with id: {user_id}'
        )
    return user

def read_user(username: str, db: Session = Depends(get_session)):
    return db.query(User).where(col(User.username)==username).first()
