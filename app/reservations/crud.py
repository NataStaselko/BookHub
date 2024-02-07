from fastapi import Depends
from sqlalchemy.orm import Session
from app.reservations.model import Reservation
from app.reservations.dto import ReservationDTO
from app.db.session import get_db


class ReservationRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, reservation_dto: ReservationDTO):
        reservation = Reservation(**reservation_dto.dict())
        self.db.add(reservation)
        self.db.commit()
        self.db.refresh(reservation)
        return reservation

    def find(self, reservation_id: int):
        return self.db.query(Reservation).filter(Reservation.id == reservation_id).first()

    def find_all(self, skip, limit):
        return self.db.query(Reservation).offset(skip).limit(limit).all()

    def update(self, reservation_id: int, is_active: bool):
        reservation_db = self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if reservation_db:
            reservation_db.isActive = is_active
            self.db.commit()
            self.db.refresh(reservation_db)
            return reservation_db

    def delete(self, reservation_id: int):
        reservation_db = self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if reservation_db:
            self.db.delete(reservation_db)
            self.db.commit()
            return True
        return False
