import os
import logging
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')


class Settings:
    PROJECT_TITLE: str = "Basic FastAPI User Management"
    PROJECT_VERSION: str = "0.0.1"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    TEST_USER_EMAIL = "test@example.com"


settings = Settings()