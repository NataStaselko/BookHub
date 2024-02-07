from fastapi import APIRouter, Depends, status, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from pydantic import parse_obj_as
from app.books.dto import BookDTO, BookResponse
from app.books.service import BookService


app = FastAPI()
router_books = APIRouter(prefix='/books', tags=['books'])


@router_books.post('/', response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book_dto: BookDTO, service: BookService = Depends()):
    book = service.create_book(book_dto)
    return BookResponse.from_orm(book)


@router_books.get('/{book_id}', response_model=BookResponse, status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int, service: BookService = Depends()):
    book = service.get_book_by_id(book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Book with id = {book_id} not found'
        )
    return BookResponse.from_orm(book)


@router_books.get('/', response_model=List[BookResponse], status_code=status.HTTP_200_OK)
async def get_list_books(skip: int = 0, limit: int = 10, service: BookService = Depends()):
    books = service.get_books(skip, limit)
    return parse_obj_as(List[BookResponse], books)


@router_books.put('/{book_id}', response_model=BookResponse, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book_dto: BookDTO, service: BookService = Depends()):
    book = service.update_book(book_id, book_dto)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Book with id = {book_id} not found'
        )
    return BookResponse.from_orm(book)


@router_books.delete('/{book_id}', status_code=status.HTTP_200_OK)
async def delete_book(book_id: int, service: BookService = Depends()):
    if not service.delete_book(book_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Book with id = {book_id} not found'
        )
    return JSONResponse(content={'message': f'Book whit id = {book_id} deleted successfully'})


@router_books.get('/filter', response_model=List[BookResponse], status_code=status.HTTP_200_OK)
async def get_filter_books(author_id: int = None, genre_id: int = None, min_price:
                           float = None, max_price: float = None, skip: int = 0,
                           limit: int = 10, service: BookService = Depends()):
    books = service.filter_books(skip, limit, author_id, genre_id, min_price, max_price)
    return parse_obj_as(list[BookResponse], books)
