from dataclasses import dataclass
from typing import Text

from interview_helper.domain.interview.interview_value_objects import QuestionId


@dataclass
class Question:
    id: QuestionId
    content: Text
