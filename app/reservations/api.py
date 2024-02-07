from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from pydantic import parse_obj_as
from app.reservations.dto import ReservationDTO, ReservationResponse
from app.reservations.service import ReservationService


router_reservations = APIRouter(prefix='/reservations', tags=['reservations'])


@router_reservations.post('/', response_model=ReservationResponse, status_code=status.HTTP_201_CREATED)
async def create_reservation(reservation_dto: ReservationDTO, service: ReservationService = Depends()):
    reservation = service.create_reservation(reservation_dto)
    return ReservationResponse.from_orm(reservation)


@router_reservations.get('/{reservation_id}', response_model=ReservationResponse, status_code=status.HTTP_200_OK)
async def get_reservation_by_id(reservation_id: int, service: ReservationService = Depends()):
    reservation = service.get_reservation_by_id(reservation_id)
    if reservation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Reservation with id = {reservation_id} not found'
        )
    return ReservationResponse.from_orm(reservation)


@router_reservations.get('/', response_model=List[ReservationResponse], status_code=status.HTTP_200_OK)
async def get_list_reservations(skip: int = 0, limit=10, service: ReservationService = Depends()):
    reservation = service.get_reservations(skip, limit)
    return parse_obj_as(List[ReservationResponse], reservation)


@router_reservations.put('/{reservation_id}', response_model=ReservationResponse, status_code=status.HTTP_200_OK)
async def update_reservation(reservation_id: int, is_active, service: ReservationService = Depends()):
    reservation = service.update_reservation(reservation_id, is_active)
    if reservation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Reservation with id = {reservation_id} not found'
        )
    return ReservationResponse.from_orm(reservation)


@router_reservations.delete('/{reservation_id}', status_code=status.HTTP_200_OK)
async def delete_reservation(reservation_id: int, service: ReservationService = Depends()):
    if not service.delete_reservation(reservation_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Reservation with id = {reservation_id} not found'
        )
    return JSONResponse(content={'message': f'Reservation whit id = {reservation_id} deleted successfully'})
