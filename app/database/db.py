from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

import os


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app/data/contacts.db")


Base = declarative_base()

engine = create_engine(
    DATABASE_URL,
    connect_args = {
        "check_same_thread": False,
    }
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)


def get_db_session():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
