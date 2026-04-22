from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class ProcessEvent(Base):
    __tablename__ = "process_events"

    id = Column(Integer, primary_key=True, index=True)

    process_id = Column(Integer, ForeignKey("processes.id"))
    process = relationship("Process", back_populates="events")

    event_type = Column(String(50))
    description = Column(String(255))

    timestamp = Column(DateTime, default=datetime.utcnow)