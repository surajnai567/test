from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:daysunmon@127.0.0.1/test"
SQLALCHEMY_DATABASE_URL = """postgres://eteunnmxstwmgc:94ec4a519ff2be01fc7260b7fa72da8848f6a02e234617c4168af5231337470e@ec2-18-235-97-230.compute-1.amazonaws.com:5432/d46rl9tcpluvr8"""



engine = create_engine(
    SQLALCHEMY_DATABASE_URL  # for postgres connect_args={"check_same_thread": False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
