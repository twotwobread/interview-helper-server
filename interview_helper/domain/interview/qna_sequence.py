from datetime import datetime
from typing import List

from pydantic import BaseModel

from interview_helper.domain.interview.qna import Qna
from interview_helper.domain.user.user import User


class QnaSequence(BaseModel):
    user: User
    main_qna: Qna
    sub_qnas: List[Qna]
    created_at: datetime
