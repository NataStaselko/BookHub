from pydantic import BaseModel


class UserDTO(BaseModel):
    login: str

    class Config:
        from_attributes = True
