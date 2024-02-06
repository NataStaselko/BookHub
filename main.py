from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.database import connect, disconnect
from app.genres.api import router_genres
from app.authors.api import router_authors
from app.users.api import router_users
from app.books.api import router_books

app = FastAPI()


@asynccontextmanager
async def lifespan(fast: FastAPI):
    connect()
    try:
        yield
    finally:
        disconnect()

app.include_router(router_genres)
app.include_router(router_authors)
app.include_router(router_users)
app.include_router(router_books)
