from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.books.model import Book
from app.books.dto import BookDTO


class BookRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, book_dto: BookDTO):
        book_db = Book(**book_dto.dict())
        self.db.add(book_db)
        self.db.commit()
        self.db.refresh(book_db)
        return book_db

    def find(self, book_id: int):
        return self.db.query(Book).filter(Book.id == book_id).first()

    def find_all(self, skip: int, limit: int):
        return self.db.query(Book).offset(skip).limit(limit).all()

    def filter(self, skip: int, limit: int, author_id: int = None,
               genre_id: int = None, min_price: float = None, max_price: float = None):
        query = self.db.query(Book)

        if author_id:
            query = query.filter(Book.author_id == author_id)

        if genre_id:
            query = query.filter(Book.genres.any(id=genre_id))

        if min_price is not None:
            query = query.filter(Book.price >= min_price)

        if max_price is not None:
            query = query.filter(Book.price <= max_price)

        return query.offset(skip).limit(limit).all()

    def update(self, book_id: int, book_dto: BookDTO):
        book_db = self.db.query(Book).filter(Book.id == book_id).first()
        for key, value in book_dto.dict(exclude_unset=True).items():
            setattr(book_db, key, value)
        self.db.commit()
        self.db.refresh(book_db)
        return book_db

    def delete(self, book_id: int):
        book_db = self.db.query(Book).filter(Book.id == book_id).first()
        if book_db:
            self.db.delete(book_db)
            self.db.commit()
            return True
        return False
