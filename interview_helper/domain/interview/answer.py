from dataclasses import dataclass
from typing import Text


@dataclass
class Answer:
    id: int
    content: Text
