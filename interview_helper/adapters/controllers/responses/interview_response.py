from typing import List

from pydantic import BaseModel

from interview_helper.adapters.controllers.responses.qna_sequence_response import (
    QnaSequenceResponseDTO,
)
from interview_helper.domain.interview.interview import Interview


class InterviewResponseDTO(BaseModel):
    interview_id: int
    registered_user_id: int
    title: str
    tags: List[str]
    description: str
    created_at: str
    updated_at: str
    qna_sequences: List[QnaSequenceResponseDTO]

    @classmethod
    def from_entity(cls, interview: Interview) -> "InterviewResponseDTO":
        return cls(
            interview_id=interview.interview_id,
            registered_user_id=interview.user.user_id,
            title=interview.title,
            tags=[tag.tag_name for tag in interview.tags],
            description=interview.description,
            created_at=interview.created_at,
            qna_sequences=[
                QnaSequenceResponseDTO.from_entity(qna_sequence)
                for qna_sequence in interview.qna_sequences
            ],
        )

    @classmethod
    def from_interviews(
        cls, interviews: List[Interview]
    ) -> List["InterviewResponseDTO"]:
        return [cls.from_entity(interview) for interview in interviews]


class CreateInterviewResponseDTO(BaseModel):
    interview_id: int
