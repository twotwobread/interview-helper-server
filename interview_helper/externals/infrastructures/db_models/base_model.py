from datetime import datetime
from typing import Optional

from sqlmodel import Column, Field, SQLModel, create_engine

from configs.config import CONFIG

POSTGRE_CONFIG = CONFIG["infra"]["postgre"]
HOST = POSTGRE_CONFIG["host"]
PORT = POSTGRE_CONFIG["port"]
USER = POSTGRE_CONFIG["user"]
PASSWORD = POSTGRE_CONFIG["pass"]
DATABASE = POSTGRE_CONFIG["database"]
DB_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"


class BaseModel(SQLModel):
    id: Optional[int] = Column(default=None, primary_key=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)


engine = create_engine(DB_URL, echo=True)
