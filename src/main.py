from fastapi import FastAPI
from users.views import router as users
from database import create_database

app = FastAPI()

@app.on_event("startup")
def on_starup():
    create_database()

app.include_router(users, prefix='/users', tags=['Users'])