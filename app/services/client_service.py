from sqlalchemy.orm import Session
from app.repositories.client_repository import ClientRepository


class ClientService:

    @staticmethod
    def create_client(db: Session, client_data):
        return ClientRepository.create(db, client_data)

    @staticmethod
    def get_clients(db: Session):
        return ClientRepository.get_all(db)

    @staticmethod
    def get_client(db: Session, client_id: int):
        return ClientRepository.get_by_id(db, client_id)

    @staticmethod
    def delete_client(db: Session, client_id: int):
        client = ClientRepository.get_by_id(db, client_id)
        if not client:
            return None

        ClientRepository.delete(db, client)
        return client