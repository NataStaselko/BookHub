from . import database
from sqlalchemy.orm import Session


def get_db() -> Session:
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
