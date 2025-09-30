from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODEL_DIR: str = "models"  # Default

settings = Settings()
