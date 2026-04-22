from pydantic import BaseModel
from typing import Optional


class ProcessBase(BaseModel):
    name: str
    status: Optional[str] = "new"
    client_id: Optional[int] = None


class ProcessCreate(ProcessBase):
    pass


class ProcessResponse(ProcessBase):
    id: int

    class Config:
        from_attributes = True