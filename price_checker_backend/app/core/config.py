from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Price Checker Backend"
    
    # Security
    SECRET_KEY: str = "changethissecuresecretkeyinproduction" 
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = "sqlite:///./sql_app.db"

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
