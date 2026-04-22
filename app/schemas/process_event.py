from pydantic import BaseModel
from typing import Optional


class ProcessEventBase(BaseModel):
    process_id: int
    event_type: str
    description: Optional[str] = None


class ProcessEventCreate(ProcessEventBase):
    pass


class ProcessEventResponse(ProcessEventBase):
    id: int

    class Config:
        from_attributes = True