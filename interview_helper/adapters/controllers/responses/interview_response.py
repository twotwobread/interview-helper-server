from typing import List

from pydantic import BaseModel

from interview_helper.adapters.controllers.responses.qna_sequence_response import (
    QnaSequenceResponseDTO,
)


class InterviewResponseDTO(BaseModel):
    interview_id: int
    registered_user_id: int
    title: str
    tags: List[str]
    description: str
    created_at: str
    updated_at: str
    qna_sequences: List[QnaSequenceResponseDTO]


class CreateInterviewResponseDTO(BaseModel):
    interview_id: int
