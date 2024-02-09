from pydantic import BaseModel
from typing import Optional


class GenreDTOCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True


class GenreDTOUpdate(BaseModel):
    name: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True


class GenreResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

