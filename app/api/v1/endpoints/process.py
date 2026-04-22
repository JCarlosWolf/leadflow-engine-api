from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.process import ProcessCreate, ProcessResponse
from app.schemas.process_full import ProcessFullResponse
from app.schemas.process_advance import ProcessAdvanceRequest
from app.services.process_service import ProcessService

router = APIRouter()


# 🔹 CREATE
@router.post("/", response_model=ProcessResponse)
def create_process(process: ProcessCreate, db: Session = Depends(get_db)):
    return ProcessService.create_process(db, process)


# 🔹 GET ALL
@router.get("/", response_model=list[ProcessResponse])
def get_processes(db: Session = Depends(get_db)):
    return ProcessService.get_processes(db)


# 🔹 GET ONE
@router.get("/{process_id}", response_model=ProcessResponse)
def get_process(process_id: int, db: Session = Depends(get_db)):
    process = ProcessService.get_process(db, process_id)
    if not process:
        raise HTTPException(status_code=404, detail="Process not found")
    return process


# 🔹 DELETE
@router.delete("/{process_id}")
def delete_process(process_id: int, db: Session = Depends(get_db)):
    process = ProcessService.delete_process(db, process_id)
    if not process:
        raise HTTPException(status_code=404, detail="Process not found")
    return {"message": "Process deleted"}


# 🔥 FULL VIEW (AGREGADO)
@router.get("/{process_id}/full", response_model=ProcessFullResponse)
def get_full_process(process_id: int, db: Session = Depends(get_db)):
    data = ProcessService.get_full_process(db, process_id)

    if not data:
        raise HTTPException(status_code=404, detail="Process not found")

    return data


# 🔥 ADVANCE PROCESS (EVENT-DRIVEN REAL)
@router.post("/{process_id}/advance")
def advance_process(
    process_id: int,
    data: ProcessAdvanceRequest,
    db: Session = Depends(get_db)
):
    updated = ProcessService.advance_process(
        db,
        process_id,
        data.event_type,
        data.description
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Process not found")

    return {
        "message": "Process advanced",
        "new_status": updated.status
    }