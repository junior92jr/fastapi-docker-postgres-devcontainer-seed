import os
import sys

from pydantic_settings import BaseSettings


def is_testing() -> bool:
    """Check if the app is running in a test environment."""
    return "pytest" in sys.modules


class Settings(BaseSettings):
    """Implements General Settings for the Application."""

    PROJECT_NAME: str = "Fast API Seed"
    VERSION: str = "v1"
    DATABASE_URI: str = "postgresql://postgres:postgres@db/postgres"

    class Config:
        case_sensitive = True


class TestSettings(Settings):
    """Implements General Settings for Testing the Application."""

    DATABASE_URI: str = os.getenv("DATABASE_URI_TEST", "")

    class Config:
        case_sensitive = True


class AppSettings:
    """Handles settings based on environment"""

    @property
    def settings(self) -> Settings:
        """Returns the appropriate settings based on the TEST_ENV variable"""

        if is_testing():
            print("---------------")
            print("soy testing ....")
            print(os.getenv("DATABASE_URI_TEST", ""))
            print(TestSettings().DATABASE_URI)
            print("---------------")
            return TestSettings()
        return Settings()


def get_app_settings():
    return AppSettings().settings
