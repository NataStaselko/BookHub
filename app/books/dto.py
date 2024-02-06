from pydantic import BaseModel
from decimal import Decimal
from typing import List
from app.authors.dto import AuthorResponse
from app.genres.dto import GenreResponse
from app.reservations.dto import ReservationResponse


class BookDTO(BaseModel):

    title: str
    price: Decimal
    num_pages: int
    author_id: int
    genres: List[int]

    class Config:
        from_attributes = True


class BookResponse(BaseModel):
    id: int
    title: str
    price: Decimal
    num_pages: int
    author: AuthorResponse
    genres: List[GenreResponse]
    reservations: List[ReservationResponse]
    is_available: bool

    class Config:
        from_attributes = True

