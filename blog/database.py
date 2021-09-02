from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

# SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'
user = config("POSTGRES_USER", cast=str)
pwd = config("POSTGRES_PASSWORD", cast=str)
db = config("POSTGRES_DB", cast=str)
host = config("POSTGRES_SERVER", cast=str)
port = config("POSTGRES_PORT", cast=int)
SQLALCHAMY_DATABASE_URL = f"postgresql://{user}:{pwd}@{host}:{port}/{db}"

# engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
#                        "check_same_thread": False})
engine = create_engine(SQLALCHAMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
