from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session

from auth.helpers import authenticate
from database import get_session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')

router = APIRouter()

@router.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    if not authenticate(form_data.username, form_data.password, db=db):
        raise HTTPException(status_code=402, detail="Invalid Credentials")
        
    return {'access_token':form_data.username, 'token_type':'bearer'}

@router.get('/')
def check_auth(token: str = Depends(oauth2_scheme)):
    return {"token": token}