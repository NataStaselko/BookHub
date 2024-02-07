from fastapi import Depends
from app.reservations.crud import ReservationRepo
from app.reservations.dto import ReservationDTO


class ReservationService:

    def __init__(self, crud: ReservationRepo = Depends()):
        self.crud = crud

    def create_reservation(self, reservation_dto: ReservationDTO):
        return self.crud.create(reservation_dto)

    def get_reservation_by_id(self, reservation_id: int):
        return self.crud.find(reservation_id)

    def get_reservations(self, skip, limit):
        return self.crud.find_all(skip, limit)

    def update_reservation(self, reservation_id: int, is_active: bool):
        return self.crud.update(reservation_id, is_active)

    def delete_reservation(self, reservation_id: int):
        return self.crud.delete(reservation_id)