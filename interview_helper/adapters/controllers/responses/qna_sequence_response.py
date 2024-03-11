from typing import List

from pydantic import BaseModel

from interview_helper.adapters.controllers.responses.qna_response import QnaResponseDTO
from interview_helper.domain.interview.qna_sequence import QnaSequence


class QnaSequenceResponseDTO(BaseModel):
    main_qna: QnaResponseDTO
    sub_qnas: List[QnaResponseDTO]

    @classmethod
    def from_entity(cls, qna_sequence: QnaSequence) -> "QnaSequenceResponseDTO":
        return cls(
            main_qna=QnaResponseDTO.from_entity(qna_sequence.main_qna),
            sub_qnas=[QnaResponseDTO.from_entity(qna) for qna in qna_sequence.sub_qnas],
        )
