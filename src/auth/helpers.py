import bcrypt
from fastapi import Depends
from sqlmodel import Session
from database import get_session
from users.crud import read_user


def authenticate(username: str, password: str,  db: Session = Depends(get_session)):
    user = read_user(username=username, db=db)
    if user:
        return bcrypt.checkpw(password.encode('utf8'), user.hashed_password.encode('utf8'))
    else:
        return False