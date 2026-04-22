from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.api.deps import get_db

api_router = APIRouter()


@api_router.get("/health")
def health_check():
    return {"status": "ok"}


@api_router.get("/db-test")
def test_db(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1")).fetchone()
    return {"db_response": result[0]}

from app.api.v1.endpoints import client

api_router.include_router(client.router, prefix="/clients", tags=["clients"])


from app.api.v1.endpoints import process

api_router.include_router(process.router, prefix="/processes", tags=["processes"])

from app.api.v1.endpoints import process_event

api_router.include_router(process_event.router, prefix="/process-events", tags=["process-events"])