import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Implements General Settings for the Application."""

    PROJECT_NAME: str = "Fast API Seed"
    VERSION: str = "v1"
    DATABASE_URI: str = os.getenv("DATABASE_URI", "")
    TEST_DATABASE_URI: str = os.getenv("DATABASE_URI_TEST", "")

    class Config:
        case_sensitive = True


settings = Settings()
