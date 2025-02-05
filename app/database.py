from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import get_app_settings

print("------------")
print(get_app_settings().DATABASE_URI)
print("------------")

engine = create_engine(get_app_settings().DATABASE_URI, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_db_and_tables() -> None:
    """Creates the tables in the database from the models."""
    Base.metadata.create_all(bind=engine)


def get_session():
    """Generates a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
