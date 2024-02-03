from pydantic import BaseModel


class AutorDTO(BaseModel):
    first_name: str
    last_name: str
    avatar: str

    class Config:
        from_attributes = True
