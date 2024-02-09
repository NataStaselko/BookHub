from fastapi import APIRouter, Depends, status, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from app.books.dto import BookDTOCreate, BookResponse, BookDTOUpdate
from app.books.service import BookService
import logging

router_books = APIRouter(prefix='/books', tags=['books'])
router_filter = APIRouter(prefix='/filter', tags=['filter'])


@router_books.post('/', response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book_dto: BookDTOCreate, service: BookService = Depends()):
    logging.debug("HELLO", book_dto.author_id)
    book = service.create_book(book_dto)
    return service.get_book_response(book)


@router_books.get('/{book_id}', response_model=BookResponse, status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int, service: BookService = Depends()):
    book = service.get_book_by_id(book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Book with id = {book_id} not found'
        )
    return service.get_book_response(book)


@router_books.get('/', response_model=List[BookResponse], status_code=status.HTTP_200_OK)
async def get_list_books(skip: int = 0, limit: int = 10, service: BookService = Depends()):
    books = service.get_books(skip, limit)
    return [service.get_book_response(book) for book in books]


@router_books.put('/{book_id}', response_model=BookResponse, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book_dto: BookDTOUpdate, service: BookService = Depends()):
    book = service.update_book(book_id, book_dto)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Book with id = {book_id} not found'
        )
    return service.get_book_response(book)


@router_books.delete('/{book_id}', status_code=status.HTTP_200_OK)
async def delete_book(book_id: int, service: BookService = Depends()):
    if not service.delete_book(book_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Book with id = {book_id} not found'
        )
    return JSONResponse(content={'message': f'Book whit id = {book_id} deleted successfully'})


@router_filter.get('/books', response_model=List[BookResponse], status_code=status.HTTP_200_OK)
async def get_filter_books(author_id: int = None, genre_id: int = None, min_price:
                           float = None, max_price: float = None, skip: int = 0,
                           limit: int = 10, service: BookService = Depends()):
    books = service.filter_books(skip, limit, author_id, genre_id, min_price, max_price)
    return [service.get_book_response(book) for book in books]
