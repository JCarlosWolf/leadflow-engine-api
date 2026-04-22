import os
from dotenv import load_dotenv

# 🔥 Forzar carga del .env desde raíz del proyecto
load_dotenv(dotenv_path=".env")


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "LeadFlow Engine API")
    API_V1_STR: str = os.getenv("API_V1_STR", "/api/leadflow")

    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "3306")
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "1234")
    DB_NAME: str = os.getenv("DB_NAME", "leadflow_db")

    @property
    def DATABASE_URL(self):
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()