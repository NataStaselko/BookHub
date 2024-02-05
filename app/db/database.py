import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base


load_dotenv('.env')

db_url = os.environ['DATABASE_URL']

engine = create_engine(db_url)

SessionLocal = sessionmaker(bind=engine)

Base: DeclarativeMeta = declarative_base()


def connect():
    Base.metadata.create_all(bind=engine)

def disconnect():
    engine.dispose()
