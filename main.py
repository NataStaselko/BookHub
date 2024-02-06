from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.database import connect, disconnect
from app.genres.api import router_genre


@asynccontextmanager
async def lifespan(fast: FastAPI):
    connect()
    try:
        yield
    finally:
        disconnect()

app = FastAPI()

app.include_router(router_genre)
