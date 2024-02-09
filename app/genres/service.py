from fastapi import Depends
from app.genres.crud import GenreRepo
from app.genres.dto import GenreDTOCreate, GenreDTOUpdate


class GenreService:

    def __init__(self, crud: GenreRepo = Depends()):
        self.crud = crud

    def create_genre(self, genre_dto: GenreDTOCreate):
        return self.crud.create(genre_dto)

    def get_genre_by_id(self, genre_id: int):
        return self.crud.find(genre_id)

    def get_genres(self, skip, limit):
        return self.crud.find_all(skip, limit)

    def update_genre(self, genre_id: int, genre_dto: GenreDTOUpdate):
        return self.crud.update(genre_id, genre_dto)

    def delete_genre(self, genre_id: int):
        return self.crud.delete(genre_id)
