from sqlalchemy.orm import Session
from app.models.client import Client


class ClientRepository:

    @staticmethod
    def create(db: Session, client_data):
        client = Client(**client_data.dict())
        db.add(client)
        db.commit()
        db.refresh(client)
        return client

    @staticmethod
    def get_all(db: Session):
        return db.query(Client).all()

    @staticmethod
    def get_by_id(db: Session, client_id: int):
        return db.query(Client).filter(Client.id == client_id).first()

    @staticmethod
    def delete(db: Session, client):
        db.delete(client)
        db.commit()