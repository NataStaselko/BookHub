from fastapi import Depends
from app.users.dto import UserDTOCreate, UserDTOUpdate
from app.users.crud import UserRepo


class UserService:

    def __init__(self, crud: UserRepo = Depends()):
        self.crud = crud

    def create_user(self, user_dto: UserDTOCreate):
        return self.crud.create(user_dto)

    def get_user_by_id(self, user_id: int):
        return self.crud.find(user_id)

    def get_users(self, skip, limit):
        return self.crud.find_all(skip, limit)

    def update_user(self, user_id: int, user_dto: UserDTOUpdate):
        return self.crud.update(user_id, user_dto)

    def delete_user(self, user_id: int):
        return self.crud.delete(user_id)
