from fastapi import Depends
from app.users.dto import UserDTO
from app.users.crud import UserRepo


class UserService:

    def __init__(self, crud: UserRepo = Depends()):
        self.crud = crud

    def create_user(self, user_dto: UserDTO):
        return self.crud.create(user_dto)

    def get_user_by_id(self, user_dto: int):
        return self.crud.find(user_dto)

    def get_users(self, skip, limit):
        return self.crud.find_all(skip, limit)

    def update_user(self, user_id: int, user_dto: UserDTO):
        return self.crud.update(user_id, user_dto)

    def delete_user(self, user_id: int):
        return self.crud.delete(user_id)
