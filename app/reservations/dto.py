from pydantic import BaseModel


class ReservationDTO(BaseModel):
    book_id: int
    user_id: int

    class Config:
        from_attributes = True
