from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from auth.helpers import authenticate, create_token, get_current_user
from database import get_session
from users.crud import read_user
from users.models import UserRead


router = APIRouter()

@router.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    if not authenticate(form_data.username, form_data.password, db=db):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    user = read_user(form_data.username, db)

    return create_token(user=user)

@router.get('/test')
def check_auth(current_user: UserRead = Depends(get_current_user)):
    return {'status':'ok'}