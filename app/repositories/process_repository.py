from sqlalchemy.orm import Session
from app.models.process import Process


class ProcessRepository:

    @staticmethod
    def create(db: Session, process_data):
        process = Process(**process_data.dict())
        db.add(process)
        db.commit()
        db.refresh(process)
        return process

    @staticmethod
    def get_all(db: Session):
        return db.query(Process).all()

    @staticmethod
    def get_by_id(db: Session, process_id: int):
        return db.query(Process).filter(Process.id == process_id).first()

    @staticmethod
    def delete(db: Session, process):
        db.delete(process)
        db.commit()