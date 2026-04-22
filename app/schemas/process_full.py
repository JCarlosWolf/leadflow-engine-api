from pydantic import BaseModel
from typing import List, Optional


class ProcessEventResponse(BaseModel):
    id: int
    event_type: str
    description: Optional[str] = None

    class Config:
        from_attributes = True


class ClientResponse(BaseModel):
    id: int
    name: str
    email: Optional[str] = None

    class Config:
        from_attributes = True


class ProcessResponse(BaseModel):
    id: int
    name: str
    status: str

    class Config:
        from_attributes = True


class ProcessFullResponse(BaseModel):
    process: ProcessResponse
    client: ClientResponse
    events: List[ProcessEventResponse]