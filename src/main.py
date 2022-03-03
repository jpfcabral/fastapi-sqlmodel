from fastapi import APIRouter, FastAPI
from users.views import router as users
from auth.views import router as auth
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
router.include_router(auth, prefix='/auth', tags=['Authentication'])
app.include_router(router)