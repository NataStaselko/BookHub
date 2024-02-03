from pydantic import BaseModel
from decimal import Decimal
from typing import List


class BookDTO(BaseModel):
    title: str
    price: Decimal
    num_pages: int
    author_id: int
    genres: List[int]
    is_available: bool

    class Config:
        from_attributes = True
