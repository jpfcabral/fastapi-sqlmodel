from fastapi import APIRouter, Depends
from sqlmodel import Session
from auth.helpers import get_current_user
from database import get_session
from users.models import UserCreate, UserRead
from users.crud import create_user, read_user_by_id

router = APIRouter()

@router.post('/', response_model=UserRead, status_code=201)
def create_a_user(user: UserCreate, db: Session = Depends(get_session)):
    return create_user(user=user, db=db)

@router.get('/me')
def get_user(current_user: UserRead = Depends(get_current_user)):
    return current_user