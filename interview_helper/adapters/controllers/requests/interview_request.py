from typing import List

from pydantic import BaseModel

from interview_helper.adapters.controllers.requests.qna_sequence_request import (
    QnaSequenceRequestDTO,
)


class InterviewRequestDTO(BaseModel):
    registered_user_id: int
    title: str
    tags: List[str]
    description: str
    qna_sequences: List[QnaSequenceRequestDTO]
