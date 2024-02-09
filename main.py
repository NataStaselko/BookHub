from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from app.db.database import connect, disconnect
from app.genres.api import router_genres
from app.authors.api import router_authors
from app.users.api import router_users
from app.books.api import router_books, router_filter
from app.reservations.api import router_reservations
from app.errors.errors import (generic_exception_handler,
                               validation_error_handler,
                               http_exception_handler)

app = FastAPI()


@asynccontextmanager
async def lifespan(fast: FastAPI):
    connect()
    try:
        yield
    finally:
        disconnect()

app.exception_handler(HTTPException)(http_exception_handler)
app.exception_handler(ValidationError)(validation_error_handler)
app.exception_handler(Exception)(generic_exception_handler)

app.include_router(router_genres)
app.include_router(router_authors)
app.include_router(router_users)
app.include_router(router_books)
app.include_router(router_filter)
app.include_router(router_reservations)
