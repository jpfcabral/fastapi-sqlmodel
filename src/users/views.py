from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from users.models import UserCreate, UserRead
from users.crud import create_user, read_user

router = APIRouter()

@router.post('/', response_model=UserRead)
def create_a_user(user: UserCreate, db: Session = Depends(get_session)):
    return create_user(user=user, db=db)

@router.get("/{user_id}", response_model=UserRead)
def get_a_user(user_id: int, db: Session = Depends(get_session)):
    return read_user(user_id=user_id, db=db)