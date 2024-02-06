from pydantic import BaseModel


class GenreDTO(BaseModel):
    name: str

    class Config:
        from_attributes = True


class GenreResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
