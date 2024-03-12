from dataclasses import dataclass

from interview_helper.domain.user.user import User

from .answer import Answer
from .question import Question


@dataclass
class Qna:
    user: User
    question: Question
    answer: Answer
