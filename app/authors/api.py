from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from pydantic import parse_obj_as
from app.authors.dto import AutorDTO, AuthorResponse
from app.authors.service import AuthorService

router_author = APIRouter(prefix='/authors', tags=['authors'])


@router_author.post('/', response_model=AuthorResponse, status_code=status.HTTP_201_CREATED)
async def create_author(author_dto: AutorDTO, service: AuthorService = Depends()):
    author = service.create_author(author_dto)
    return AuthorResponse.from_orm(author)


@router_author.get('/{author_id}', response_model=AuthorResponse, status_code=status.HTTP_200_OK)
async def get_author_by_id(author_id: int, service: AuthorService = Depends()):
    author = service.get_author_by_id(author_id)
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Author with id = {author_id} not found'
        )
    return AuthorResponse.from_orm(author)


@router_author.get('/', response_model=List[AuthorResponse], status_code=status.HTTP_200_OK)
async def get_list_authors(skip: int = 0, limit: int = 10, service: AuthorService = Depends()):
    authors = service.get_authors(skip, limit)
    return parse_obj_as(List[AuthorResponse], authors)


@router_author.put('/{author_id}', response_model=AuthorResponse, status_code=status.HTTP_200_OK)
async def update_author(author_id: int, author_dto: AutorDTO, service: AuthorService = Depends()):
    author = service.update_author(author_id, author_dto)
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Author with id = {author_id} not found'
        )
    return AuthorResponse.from_orm(author)


@router_author.delete('/{author_id}', response_model=AuthorResponse, status_code=status.HTTP_200_OK)
async def delete_author(author_id: int, service: AuthorService = Depends()):
    if not service.delete_author(author_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Author with id = {author_id} not found'
        )
