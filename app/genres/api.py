from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from pydantic import parse_obj_as
from app.genres.dto import GenreDTO, GenreResponse
from app.genres.service import GenreService


router_genres = APIRouter(prefix='/genres', tags=['genres'])


@router_genres.post('/', response_model=GenreResponse, status_code=status.HTTP_201_CREATED)
async def create_genre(genre_dto: GenreDTO, service: GenreService = Depends()):
    genre = service.create_genre(genre_dto)
    return GenreResponse.from_orm(genre)


@router_genres.get('/{genre_id}', response_model=GenreResponse, status_code=status.HTTP_200_OK)
async def get_genre_by_id(genre_id: int, service: GenreService = Depends()):
    genre = service.get_genre_by_id(genre_id)
    if genre is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Genre with id = {genre_id} not found'
        )
    return GenreResponse.from_orm(genre)


@router_genres.get('/', response_model=List[GenreResponse], status_code=status.HTTP_200_OK)
async def get_list_genres(skip: int = 0, limit=10, service: GenreService = Depends()):
    genres = service.get_genres(skip, limit)
    return parse_obj_as(List[GenreResponse], genres)


@router_genres.put('/{genre_id}', response_model=GenreResponse, status_code=status.HTTP_200_OK)
async def update_genre(genre_id: int, genre_dto: GenreDTO, service: GenreService = Depends()):
    genre = service.update_genre(genre_id, genre_dto)
    if genre is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Genre with id = {genre_id} not found'
        )
    return GenreResponse.from_orm(genre)


@router_genres.delete('/{genre_id}', status_code=status.HTTP_200_OK)
async def delete_genre(genre_id: int, service: GenreService = Depends()):
    if not service.delete_genre(genre_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Genre with id = {genre_id} not found'
        )
    return JSONResponse(content={'message': f'Genre whit id = {genre_id} deleted successfully'})
