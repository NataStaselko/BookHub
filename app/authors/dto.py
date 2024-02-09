from pydantic import BaseModel
from typing import Optional


class AutorDTOCreate(BaseModel):
    first_name: str
    last_name: str
    avatar: str

    class Config:
        from_attributes = True


class AutorDTOUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True


class AuthorResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    avatar: str

    class Config:
        from_attributes = True
