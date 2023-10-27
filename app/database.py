from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@127.0.0.1:3306/djib"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)

db_session = SessionLocal()

Base = declarative_base()

def init_db():
    from .models import User  # if need we can adjust the import to import all models
    Base.metadata.create_all(bind=engine)
