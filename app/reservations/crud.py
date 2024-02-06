from fastapi import Depends
from sqlalchemy.orm import Session
from app.reservations.model import Reservation
from app.reservations.dto import ReservationDTO
from app.db.session import get_db


class ReservationRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, reservationDTO: ReservationDTO) -> Reservation:
        reservation = Reservation(user_id=reservationDTO.user_id)
        self.db.add(reservation)
        self.db.commit()
        self.db.refresh(reservation)
        return reservation
