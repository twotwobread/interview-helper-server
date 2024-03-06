from dataclasses import dataclass
from typing import Text

from interview_helper.domain.interview.interview_value_objects import AnswerId


@dataclass
class Answer:
    id: AnswerId
    content: Text
