import bcrypt
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from database import get_session
from users.crud import read_user
from users.models import User, UserRead
from config import settings
from auth.models import Token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')

def authenticate(username: str, password: str,  db: Session = Depends(get_session)):
    user = read_user(username=username, db=db)
    if user:
        return bcrypt.checkpw(password.encode('utf8'), user.hashed_password.encode('utf8'))
    else:
        return False

def create_token(user: User):
    user_obj = UserRead.from_orm(user)
    token = jwt.encode(user_obj.dict(), settings.SECRET_KEY, settings.ALGORITHM)
    response = Token(access_token=token, token_type='bearer')

    return response.dict()

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        user = read_user(username=payload['username'], db=db)
    except Exception as e:
        raise HTTPException(status_code=401, detail='Invalid Credentials')
    
    return UserRead.from_orm(user)
