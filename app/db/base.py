from sqlalchemy.orm import declarative_base

# Base principal para todos los modelos ORM
Base = declarative_base()

# 🔥 IMPORTANTE: importar TODOS los modelos para que SQLAlchemy los registre
from app.models.user import User
from app.models.role import Role
from app.models.client import Client
from app.models.process import Process
from app.models.process_event import ProcessEvent