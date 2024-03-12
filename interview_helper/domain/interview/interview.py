from datetime import datetime
from typing import List

from pydantic import BaseModel

from interview_helper.domain.interview.qna_sequence import QnaSequence
from interview_helper.domain.interview.tag import Tag
from interview_helper.domain.user.user import User


class Interview(BaseModel):
    interview_id: int
    title: str
    description: str
    user: User
    qna_sequences: List[QnaSequence]
    tags: List[Tag]
    created_at: datetime
