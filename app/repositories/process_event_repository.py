from sqlalchemy.orm import Session
from app.models.process_event import ProcessEvent


class ProcessEventRepository:

    @staticmethod
    def create(db: Session, event_data):
        event = ProcessEvent(**event_data.dict())
        db.add(event)
        db.commit()
        db.refresh(event)
        return event

    @staticmethod
    def get_by_process(db: Session, process_id: int):
        return db.query(ProcessEvent).filter(ProcessEvent.process_id == process_id).all()