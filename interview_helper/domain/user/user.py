from dataclasses import dataclass
from datetime import datetime

from interview_helper.domain.user.user_value_objects import UserId


@dataclass
class User:
    id: UserId
    name: str
    password: str
    email: str
    registered_at: datetime
