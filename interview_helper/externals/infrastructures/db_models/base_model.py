from datetime import datetime
from typing import Optional

from sqlmodel import Column, Field, Session, SQLModel, create_engine


class BaseModel(SQLModel):
    id: Optional[int] = Column(default=None, primary_key=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)


engine = create_engine("sqlite:///db.sqlite")
SESSION = Session(engine)
