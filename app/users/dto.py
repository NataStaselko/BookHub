from pydantic import BaseModel
from typing import Optional


class UserDTOCreate(BaseModel):
    login: str

    class Config:
        from_attributes = True


class UserDTOUpdate(BaseModel):
    login: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True


class UserResponse(BaseModel):
    id: int
    login: str

    class Config:
        from_attributes = True
