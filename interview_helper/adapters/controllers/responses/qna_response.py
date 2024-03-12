from pydantic import BaseModel

from interview_helper.domain.interview.qna import Qna


class QnaResponseDTO(BaseModel):
    question: str
    answer: str

    @classmethod
    def from_entity(cls, qna: Qna) -> "QnaResponseDTO":
        return cls(question=qna.question.content, answer=qna.answer.content)
