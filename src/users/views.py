from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from users.models import UserCreate, UserRead
from users.crud import create_user

router = APIRouter()

@router.post('/', response_model=UserRead)
def create_a_user(user: UserCreate, db: Session = Depends(get_session)):
    return create_user(user=user, db=db)
