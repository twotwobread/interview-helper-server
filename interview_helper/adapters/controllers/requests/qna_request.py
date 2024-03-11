from pydantic import BaseModel


class QnaRequestDTO(BaseModel):
    question: str
    answer: str
