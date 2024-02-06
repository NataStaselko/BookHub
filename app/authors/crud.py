from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.authors.model import Author
from app.authors.dto import AutorDTO, AuthorResponse

dog
class AuthorRepo:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, author_dto: AutorDTO):
        author_db = Author(**author_dto.dict())
        self.db.add(author_db)
        self.db.commit()
        self.db.refresh(author_db)
        return author_db
