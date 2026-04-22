from app.db.base import Base
from app.db.session import engine


def init_db():
    """
    Crea todas las tablas en la base de datos
    basadas en los modelos definidos.
    """
    Base.metadata.create_all(bind=engine)