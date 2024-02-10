from pydantic import BaseModel
from decimal import Decimal


class BookResponseByReservation(BaseModel):
    id: int
    title: str
    price: Decimal
    is_available: bool

    class Config:
        from_attributes = True
