from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.process_event import ProcessEventCreate, ProcessEventResponse
from app.services.process_event_service import ProcessEventService

router = APIRouter()


@router.post("/", response_model=ProcessEventResponse)
def create_event(event: ProcessEventCreate, db: Session = Depends(get_db)):
    result = ProcessEventService.create_event(db, event)
    if not result:
        raise HTTPException(status_code=404, detail="Process not found")
    return result


@router.get("/{process_id}", response_model=list[ProcessEventResponse])
def get_events(process_id: int, db: Session = Depends(get_db)):
    return ProcessEventService.get_events(db, process_id)