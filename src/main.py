from fastapi import APIRouter, FastAPI
from users.views import router as users
from database import create_database

app = FastAPI()
router = APIRouter()

@app.on_event("startup")
def on_starup():
    create_database()

@router.get('/')
def index():
    return {'status':'ok'}

router.include_router(users, prefix='/users', tags=['Users'])
app.include_router(router)