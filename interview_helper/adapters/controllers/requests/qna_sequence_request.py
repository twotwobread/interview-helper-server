from typing import List

from pydantic import BaseModel

from interview_helper.adapters.controllers.requests.qna_request import QnaRequestDTO


class QnaSequenceRequestDTO(BaseModel):
    main_qna: QnaRequestDTO
    sub_qnas: List[QnaRequestDTO]
