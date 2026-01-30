from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    PROJECT_NAME: str = "TaskFlow"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    
    # Firebase
    FIREBASE_CREDENTIALS_PATH: str = "keys/taskflow-ddf5c-firebase-adminsdk-fbsvc-66a50887bb.json"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()