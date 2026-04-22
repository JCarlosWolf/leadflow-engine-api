from sqlalchemy.orm import Session

from app.repositories.process_repository import ProcessRepository
from app.models.process import Process
from app.models.client import Client
from app.models.process_event import ProcessEvent


class ProcessService:

    @staticmethod
    def create_process(db: Session, process_data):
        return ProcessRepository.create(db, process_data)

    @staticmethod
    def get_processes(db: Session):
        return ProcessRepository.get_all(db)

    @staticmethod
    def get_process(db: Session, process_id: int):
        return ProcessRepository.get_by_id(db, process_id)

    @staticmethod
    def delete_process(db: Session, process_id: int):
        process = ProcessRepository.get_by_id(db, process_id)
        if not process:
            return None

        ProcessRepository.delete(db, process)
        return process

    # 🔥 FULL PROCESS (AGREGADO)
    @staticmethod
    def get_full_process(db: Session, process_id: int):
        process = db.query(Process).filter(Process.id == process_id).first()

        if not process:
            return None

        client = db.query(Client).filter(Client.id == process.client_id).first()

        events = db.query(ProcessEvent).filter(
            ProcessEvent.process_id == process_id
        ).all()

        return {
            "process": process,
            "client": client,
            "events": events
        }

    # 🔥 AVANZAR PROCESO (EVENT-DRIVEN)
    @staticmethod
    def advance_process(
        db: Session,
        process_id: int,
        event_type: str,
        description: str = None
    ):
        process = ProcessRepository.get_by_id(db, process_id)

        if not process:
            return None

        # 1. Crear evento
        event = ProcessEvent(
            process_id=process_id,
            event_type=event_type,
            description=description
        )
        db.add(event)

        # 2. Actualizar estado automáticamente
        process.status = ProcessService.map_event_to_status(event_type)

        db.commit()
        db.refresh(process)

        return process

    # 🔥 MOTOR DE ESTADOS
    @staticmethod
    def map_event_to_status(event_type: str) -> str:
        mapping = {
            "new": "new",
            "contacted": "contacted",
            "follow_up": "in_progress",
            "closed": "closed",
            "lost": "lost"
        }

        return mapping.get(event_type, "new")