from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from pydantic import parse_obj_as
from app.users.dto import UserDTO, UserResponse
from app.users.service import UserService

router_users = APIRouter(prefix='/users', tags=['users'])


@router_users.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_dto: UserDTO, service: UserService = Depends()):
    user = service.create_user(user_dto)
    return UserResponse.from_orm(user)


@router_users.get('/{user_id}', response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, service: UserService = Depends()):
    user = service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id = {user_id} not found'
        )
    return UserResponse.from_orm(user)


@router_users.get('/', response_model=List[UserResponse], status_code=status.HTTP_200_OK)
async def get_list_users(skip: int = 0, limit: int = 10, service: UserService = Depends()):
    users = service.get_users(skip, limit)
    return parse_obj_as(List[UserResponse], users)


@router_users.put('/{user_id}', response_model=UserResponse, status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user_dto: UserDTO, service: UserService = Depends()):
    user = service.update_user(user_id, user_dto)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id = {user_id} not found'
        )
    return UserResponse.from_orm(user)


@router_users.delete('/{user_id}', status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, service: UserService = Depends()):
    if not service.delete_user(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id = {user_id} not found'
        )
    return JSONResponse(content={'message': f'User whit id = {user_id} deleted successfully'})
