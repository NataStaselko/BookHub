from fastapi import Depends
from app.authors.dto import AutorDTO
from app.authors.crud import AuthorRepo


class AuthorService:

    def __init__(self, crud: AuthorRepo = Depends()):
        self.crud = crud

    def create_author(self, author_dto: AutorDTO):
        return self.crud.create(author_dto)

    def get_author_by_id(self, author_dto: int):
        return self.crud.find(author_dto)

    def get_authors(self, skip, limit):
        return self.crud.find_all(skip, limit)

    def update_author(self, author_id: int, author_dto: AutorDTO):
        return self.crud.update(author_id, author_dto)

    def delete_author(self, author_id: int):
        return self.crud.delete(author_id)





