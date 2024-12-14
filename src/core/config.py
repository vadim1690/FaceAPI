from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    LOG_LEVEL: str

    class Config:
        env_file = ".env"

settings = Settings()
