from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:daysunmon@127.0.0.1/test"
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")


engine = create_engine(
    SQLALCHEMY_DATABASE_URL  # for postgres connect_args={"check_same_thread": False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
