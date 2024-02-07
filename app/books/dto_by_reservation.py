from pydantic import BaseModel
from decimal import Decimal
from typing import List
from app.authors.dto import AuthorResponse
from app.genres.dto import GenreResponse


class BookResponseByReservation(BaseModel):
    id: int
    title: str
    price: Decimal
    num_pages: int
    author: AuthorResponse
    genres: List[GenreResponse]
    is_available: bool

    class Config:
        from_attributes = True