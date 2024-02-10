from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from app.reservations.dto import ReservationDTCreate, ReservationResponse
from app.reservations.service import ReservationService


router_reservations = APIRouter(prefix='/reservations', tags=['reservations'])


@router_reservations.post('/', response_model=ReservationResponse, status_code=status.HTTP_201_CREATED)
async def create_reservation(reservation_dto: ReservationDTCreate, service: ReservationService = Depends()):
    reservation = service.create_reservation(reservation_dto)
    if reservation is None:
        return JSONResponse(content={'message': f'Reservation whit '
                                                f'book_id = {reservation_dto.book_id} is not available'})
    return service.get_reservation_response(reservation)


@router_reservations.get('/{reservation_id}', response_model=ReservationResponse, status_code=status.HTTP_200_OK)
async def get_reservation_by_id(reservation_id: int, service: ReservationService = Depends()):
    reservation = service.get_reservation_by_id(reservation_id)
    if reservation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Reservation with id = {reservation_id} not found'
        )
    return service.get_reservation_response(reservation)


@router_reservations.get('/', response_model=List[ReservationResponse], status_code=status.HTTP_200_OK)
async def get_list_reservations(skip: int = 0, limit=10, service: ReservationService = Depends()):
    reservations = service.get_reservations(skip, limit)
    return [service.get_reservation_response(reservation) for reservation in reservations]

# Этот запрос обновляет поле is_active на False в сущности Reservation
# меняется поле is_available в Book на True

@router_reservations.put('/{reservation_id}', response_model=ReservationResponse, status_code=status.HTTP_200_OK)
async def update_reservation(reservation_id: int, service: ReservationService = Depends()):
    reservation = service.update_reservation(reservation_id)
    if reservation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Reservation with id = {reservation_id} not found'
        )
    return service.get_reservation_response(reservation)


# При удалении reservation, меняется поле is_available в Book на True
@router_reservations.delete('/{reservation_id}', status_code=status.HTTP_200_OK)
async def delete_reservation(reservation_id: int, service: ReservationService = Depends()):
    if not service.delete_reservation(reservation_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Reservation with id = {reservation_id} not found'
        )
    return JSONResponse(content={'message': f'Reservation whit id = {reservation_id} deleted successfully'})
