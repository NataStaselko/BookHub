from pydantic import BaseModel
from datetime import datetime
from app.users.dto import UserResponse
from app.books.dto_by_reservation import BookResponseByReservation


class ReservationDTCreate(BaseModel):
    book_id: int
    user_id: int

    class Config:
        from_attributes = True


class ReservationResponse(BaseModel):
    id: int
    book: BookResponseByReservation
    user: UserResponse
    time_start: datetime
    time_end: datetime
    is_active: bool

    class Config:
        json_encoders = {
            datetime: lambda dt: dt.strftime("%d-%m-%Y")
        }
        from_attributes = True
