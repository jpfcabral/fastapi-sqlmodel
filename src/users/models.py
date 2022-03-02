from typing import Optional
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    active: Optional[bool] = Field(default=True)
    super_user: Optional[bool] = Field(default=False)

class UserCreate(SQLModel):
    username: str
    hashed_password: str

class UserRead(SQLModel):
    id: int
    username: str
    active: bool
    super_user: bool