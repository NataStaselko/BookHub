from fastapi import Depends
from sqlalchemy.orm import Session
from app.reservations.model import Reservation
from app.books.model import Book
from app.reservations.dto import ReservationDTCreate
from app.db.session import get_db


class ReservationRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, reservation_dto: ReservationDTCreate):
        book = self.db.query(Book).filter(Book.id == reservation_dto.book_id).first()
        if book and book.is_available:
            reservation = Reservation(**reservation_dto.dict())
            self.db.add(reservation)
            book.is_available = False
            self.db.commit()
            self.db.refresh(reservation)
            return reservation
        return None

    def find(self, reservation_id: int):
        return self.db.query(Reservation).filter(Reservation.id == reservation_id).first()

    def find_all(self, skip, limit):
        return self.db.query(Reservation).offset(skip).limit(limit).all()

    def update(self, reservation_id: int):
        reservation_db = self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
        reservation_db.is_active = False
        book = self.db.query(Book).filter(Book.id == int(reservation_db.book_id)).first()
        book.is_available = True
        self.db.commit()
        self.db.refresh(reservation_db)
        return reservation_db

    def delete(self, reservation_id: int):
        reservation_db = self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if reservation_db:
            book = self.db.query(Book).filter(Book.id == int(reservation_db.book_id)).first()
            book.is_available = True
            self.db.delete(reservation_db)
            self.db.commit()
            return True
        return False




