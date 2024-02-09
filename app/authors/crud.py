from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.authors.model import Author
from app.authors.dto import AutorDTOCreate, AutorDTOUpdate


class AuthorRepo:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, author_dto: AutorDTOCreate):
        author_db = Author(**author_dto.dict())
        self.db.add(author_db)
        self.db.commit()
        self.db.refresh(author_db)
        return author_db

    def find(self, author_id: int):
        return self.db.query(Author).filter(Author.id == author_id).first()

    def find_all(self, skip: int, limit: int):
        return self.db.query(Author).offset(skip).limit(limit).all()

    def update(self, author_id: int, author_dto: AutorDTOUpdate):
        author_db = self.db.query(Author).filter(Author.id == author_id).first()
        if author_db:
            for key, value in author_dto.dict(exclude_unset=True).items():
                if value is not None:
                    setattr(author_db, key, value)
            self.db.commit()
            self.db.refresh(author_db)
            return author_db

    def delete(self, author_id: int):
        author_db = self.db.query(Author).filter(Author.id == author_id).first()
        if author_db:
            self.db.delete(author_db)
            self.db.commit()
            return True
        return False
