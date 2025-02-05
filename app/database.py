from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import settings
from app.utils.common import is_testing

engine = create_engine(
    settings.DATABASE_URI if not is_testing(
    ) else settings.TEST_DATABASE_URI, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_db_and_tables() -> None:
    """Creates the tables in the database from the models."""
    Base.metadata.create_all(bind=engine)


def drop_db_and_tables() -> None:
    """Drops the tables in the database, clearing all data."""
    Base.metadata.drop_all(bind=engine)


def get_session():
    """Generates a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
