from pydantic import BaseModel, EmailStr
from typing import Optional


class ClientBase(BaseModel):
    name: str
    email: Optional[EmailStr] = None


class ClientCreate(ClientBase):
    pass


class ClientResponse(ClientBase):
    id: int

    class Config:
        from_attributes = True