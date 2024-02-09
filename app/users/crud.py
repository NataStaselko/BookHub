from fastapi import Depends
from sqlalchemy.orm import Session
from app.users.model import User
from app.users.dto import UserDTOCreate, UserDTOUpdate
from app.db.session import get_db


class UserRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, user_dto: UserDTOCreate):
        user_db = User(**user_dto.dict())
        self.db.add(user_db)
        self.db.commit()
        self.db.refresh(user_db)
        return user_db

    def find(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def find_all(self, skip: int, limit: int):
        return self.db.query(User).offset(skip).limit(limit).all()

    def update(self, user_id: int, user_dto: UserDTOUpdate):
        user_db = self.db.query(User).filter(User.id == user_id).first()
        if user_db:
            for key, value in user_dto.dict(exclude_unset=True).items():
                if value is not None:
                    setattr(user_db, key, value)
            self.db.commit()
            self.db.refresh(user_db)
            return user_db

    def delete(self, user_id: int):
        user_db = self.db.query(User).filter(User.id == user_id).first()
        if user_db:
            self.db.delete(user_db)
            self.db.commit()
            return True
        return False

