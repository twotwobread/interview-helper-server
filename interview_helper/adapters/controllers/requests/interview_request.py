from typing import List

from pydantic import BaseModel

from interview_helper.adapters.controllers.requests.qna_sequence_request import (
    QnaSequenceRequestDTO,
)

# from interview_helper.domain.interview.interview import Interview


class InterviewRequestDTO(BaseModel):
    registered_user_id: int
    title: str
    tags: List[str]
    description: str
    qna_sequences: List[QnaSequenceRequestDTO]

    # @classmethod
    # def to_entity(cls, interview_request: "InterviewRequestDTO") -> Interview:
    #     return Interview(
    #         user=User(user_id=interview_request.registered_user_id),
    #         title=interview_request.title,
    #         tags=[Tag(tag_name=tag) for tag in interview_request.tags],
    #         description=interview_request.description,
    #         qna_sequences=[
    #             QnaSequence.to_entity(qna_sequence)
    #             for qna_sequence in interview_request.qna_sequences
    #         ],
    #     )
