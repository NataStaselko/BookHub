from pydantic import BaseModel


class GenreDTO(BaseModel):
    name: str

    class Config:
        from_attributes = True
