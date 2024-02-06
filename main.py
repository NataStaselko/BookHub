from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.database import connect, disconnect
from app.genres.api import router_genre
from app.authors.api import router_author


@asynccontextmanager
async def lifespan(fast: FastAPI):
    connect()
    try:
        yield
    finally:
        disconnect()

app = FastAPI()

app.include_router(router_genre)
app.include_router(router_author)
