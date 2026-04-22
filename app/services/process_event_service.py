from sqlalchemy.orm import Session
from app.repositories.process_event_repository import ProcessEventRepository
from app.repositories.process_repository import ProcessRepository


class ProcessEventService:

    @staticmethod
    def create_event(db: Session, event_data):
        # Validar que el proceso existe
        process = ProcessRepository.get_by_id(db, event_data.process_id)
        if not process:
            return None

        # Crear evento
        event = ProcessEventRepository.create(db, event_data)

        # 🔥 ACTUALIZAR STATUS DEL PROCESO (CLAVE)
        process.status = event_data.event_type
        db.commit()

        return event

    @staticmethod
    def get_events(db: Session, process_id: int):
        return ProcessEventRepository.get_by_process(db, process_id)