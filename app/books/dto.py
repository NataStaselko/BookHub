from pydantic import BaseModel
from decimal import Decimal
from typing import List, Optional
from app.authors.dto import AuthorResponse
from app.genres.dto import GenreResponse


class BookDTOCreate(BaseModel):

    title: str
    price: Decimal
    num_pages: int
    author_id: int
    genres: List[int]

    class Config:
        from_attributes = True


class BookDTOUpdate(BaseModel):

    title: Optional[str] = None
    price: Optional[Decimal] = None
    num_pages: Optional[int] = None
    author_id: Optional[int] = None
    genres: Optional[List[int]] = None

    class Config:
        arbitrary_types_allowed = True


class BookResponse(BaseModel):
    id: int
    title: str
    price: Decimal
    num_pages: int
    author: AuthorResponse
    genres: List[GenreResponse]
    is_available: bool

    class Config:

        from_attributes = True
