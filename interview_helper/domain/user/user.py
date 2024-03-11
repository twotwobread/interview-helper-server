from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    user_id: int
    name: str
    password: str
    email: str
    registered_at: datetime
