from fastapi import Depends
from app.reservations.model import Reservation
from app.reservations.crud import ReservationRepo
from app.reservations.dto import ReservationDTCreate, ReservationResponse
from app.users.service import UserService
from app.users.dto import UserResponse
from app.books.dto_by_reservation import BookResponseByReservation
from app.books.service import BookService


class ReservationService:

    def __init__(self, crud: ReservationRepo = Depends(),
                 user_service: UserService = Depends(),
                 book_service: BookService=Depends()):
        self.crud = crud
        self.user_service = user_service
        self.book_service = book_service

    def create_reservation(self, reservation_dto: ReservationDTCreate):
        return self.crud.create(reservation_dto)

    def get_reservation_by_id(self, reservation_id: int):
        return self.crud.find(reservation_id)

    def get_reservations(self, skip, limit):
        return self.crud.find_all(skip, limit)

    def update_reservation(self, reservation_id: int):
        return self.crud.update(reservation_id)

    def delete_reservation(self, reservation_id: int):
        return self.crud.delete(reservation_id)

    def get_reservation_response(self, reservation: Reservation) -> ReservationResponse:
        user = UserResponse.from_orm(self.user_service.get_user_by_id(reservation.user_id))
        book = BookResponseByReservation.from_orm(self.book_service.get_book_by_id(reservation.book_id))
        return ReservationResponse(id=reservation.id,
                                   book=book.dict(),
                                   user=user.dict(),
                                   time_start=reservation.time_start,
                                   time_end=reservation.time_end,
                                   is_active=reservation.is_active)
