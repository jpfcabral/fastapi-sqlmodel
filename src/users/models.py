from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, String


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str  = Field(sa_column=Column("username", String, unique=True))
    email: str = Field(sa_column=Column("email", String, unique=True))
    hashed_password: str
    active: Optional[bool] = Field(default=True)
    super_user: Optional[bool] = Field(default=False)
    date_join: Optional[datetime] = Field(default=datetime.utcnow())


class UserCreate(SQLModel):
    username: str
    email: str
    password: str


class UserRead(SQLModel):
    id: int
    username: str
    active: bool