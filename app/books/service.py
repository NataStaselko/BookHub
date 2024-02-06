from fastapi import Depends
from app.books.dto import BookDTO
from app.books.crud import BookRepo


class BookService:

    def __init__(self, crud: BookRepo = Depends()):
        self.crud = crud

    def create_book(self, book_dto: BookDTO):
        return self.crud.create(book_dto)

    def get_book_by_id(self, book_id: int):
        return self.crud.find(book_id)

    def get_books(self, skip: int, limit: int):
        return self.crud.find_all(skip, limit)

    def filter_books(self, skip: int, limit: int, author_id: int,
                     genre_id: int, min_price: float, max_price: float):
        return self.crud.filter(skip, limit, author_id, genre_id, min_price, max_price)

    def update_book(self, book_id, book_dto: BookDTO):
        return self.crud.update(book_id, book_dto)

    def delete_book(self, book_id):
        return self.crud.delete(book_id)
