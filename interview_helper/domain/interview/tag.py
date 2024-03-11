from pydantic import BaseModel


class Tag(BaseModel):
    tag_id: int
    tag_name: str
