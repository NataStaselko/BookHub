from fastapi import Depends
from app.books.model import Book
from app.books.dto import BookDTOCreate, BookDTOUpdate, BookResponse
from app.books.crud import BookRepo
from app.authors.dto import AuthorResponse
from app.authors.service import AuthorService
from app.genres.service import GenreService


class BookService:

    def __init__(self, crud: BookRepo = Depends(),
                 author_service: AuthorService = Depends(),
                 genre_service: GenreService = Depends()):
        self.crud = crud
        self.author_service = author_service
        self.genre_service = genre_service

    def create_book(self, book_dto: BookDTOCreate) -> Book:
        return self.crud.create(book_dto)

    def get_book_by_id(self, book_id: int) -> Book:
        return self.crud.find(book_id)

    def get_books(self, skip: int, limit: int):
        return self.crud.find_all(skip, limit)

    def filter_books(self, skip: int, limit: int, author_id: int,
                     genre_id: int, min_price: float, max_price: float) -> Book:
        return self.crud.filter(skip, limit, author_id, genre_id, min_price, max_price)

    def update_book(self, book_id, book_dto: BookDTOUpdate) -> Book:
        return self.crud.update(book_id, book_dto)

    def delete_book(self, book_id) -> Book:
        return self.crud.delete(book_id)

    def get_book_response(self, book: Book) -> BookResponse:
        author = None
        if book.author_id is not None:
            author = AuthorResponse.from_orm(self.author_service.get_author_by_id(book.author_id))
        genres = [genre_id for genre_id in book.genres]
        return BookResponse(id=book.id,
                            title=book.title,
                            price=float(book.price),
                            num_pages=book.num_pages,
                            author=author.dict(),
                            genres=genres,
                            is_available=book.is_available)


