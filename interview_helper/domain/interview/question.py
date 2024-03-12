from dataclasses import dataclass
from typing import Text


@dataclass
class Question:
    id: int
    content: Text
