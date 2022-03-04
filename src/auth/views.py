from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session

from auth.helpers import authenticate, create_token, get_current_user
from database import get_session
from users.crud import read_user
from users.models import UserRead


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')

router = APIRouter()

@router.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    if not authenticate(form_data.username, form_data.password, db=db):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    user = read_user(form_data.username, db)

    return create_token(user=user)

@router.get('/', response_model=UserRead)
def check_auth(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    print(token)
    return get_current_user(token=token, db=db)