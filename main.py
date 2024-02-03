from fastapi import FastAPI
from app.db.database import connect, disconnect

app = FastAPI()

connect()
