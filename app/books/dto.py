from pydantic import BaseModel
from decimal import Decimal
from typing import List, Optional


class BookDTO(BaseModel):
    id: Optional[int]
    title: str
    price: Decimal
    num_pages: int
    author_id: int
    genres: List[int]
    is_available = Optional[bool]

    class Config:
        from_attributes = True



