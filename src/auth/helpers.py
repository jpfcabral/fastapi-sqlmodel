import bcrypt
import jwt
from fastapi import Depends
from sqlmodel import Session
from database import get_session
from users.crud import read_user
from users.models import User, UserRead
from config import settings
from auth.models import Token


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
