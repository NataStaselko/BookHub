from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.database import connect, disconnect


@asynccontextmanager
async def lifespan(app: FastAPI):
    connect()
    try:
        yield
    finally:
        disconnect()


app = FastAPI()
@app.get("/")
async def root():
    return {"mess": "Hello"}
