from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.genres.model import Genre
from app.genres.dto import GenreDTOCreate, GenreDTOUpdate


class GenreRepo:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, genre_dto: GenreDTOCreate):
        genre_db = Genre(**genre_dto.dict())
        self.db.add(genre_db)
        self.db.commit()
        self.db.refresh(genre_db)
        return genre_db

    def find(self, genre_id: int):
        return self.db.query(Genre).filter(Genre.id == genre_id).first()

    def find_all(self, skip, limit):
        return self.db.query(Genre).offset(skip).limit(limit).all()

    def update(self, genre_id: int, genre_dto: GenreDTOUpdate):
        genre_db = self.db.query(Genre).filter(Genre.id == genre_id).first()
        if genre_db:
            for key, value in genre_dto.dict(exclude_unset=True).items():
                if value is not None:
                    setattr(genre_db, key, value)
            self.db.commit()
            self.db.refresh(genre_db)
            return genre_db

    def delete(self, genre_id: int):
        genre_db = self.db.query(Genre).filter(Genre.id == genre_id).first()
        if genre_db:
            self.db.delete(genre_db)
            self.db.commit()
            return True
        return False
