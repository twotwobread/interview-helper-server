from pydantic import BaseModel


class QnaResponseDTO(BaseModel):
    question: str
    answer: str
