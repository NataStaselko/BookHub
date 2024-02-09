from pydantic import BaseModel
from decimal import Decimal
from typing import List
from app.authors.dto import AuthorResponse
from app.genres.dto import GenreResponse


class BookResponseByReservation(BaseModel):
    id: int
    title: str
    price: Decimal

    class Config:
        from_attributes = True
