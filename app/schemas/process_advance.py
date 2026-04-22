from pydantic import BaseModel
from typing import Optional


class ProcessAdvanceRequest(BaseModel):
    event_type: str
    description: Optional[str] = None
