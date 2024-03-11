from typing import List

from pydantic import BaseModel

from interview_helper.adapters.controllers.responses.qna_response import QnaResponseDTO


class QnaSequenceResponseDTO(BaseModel):
    main_qna: QnaResponseDTO
    sub_qnas: List[QnaResponseDTO]
