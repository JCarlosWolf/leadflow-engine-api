from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Process(Base):
    __tablename__ = "processes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    status = Column(String(50), default="pending")

    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client")

    events = relationship("ProcessEvent", back_populates="process")