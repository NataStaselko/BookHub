from  fastapi import Depends
from sqlalchemy.orm import Session
from app.users.model import User
from app.users.dto import UserDTO
from app.db.session import get_db


class UserRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, userDTO: UserDTO) -> User:
        user = User(login=userDTO.login)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

