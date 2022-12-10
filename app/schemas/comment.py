from pydantic import BaseModel
from typing import Optional

class Comment(BaseModel):
    id: Optional[int]=1
    comment_text: str
    label: int

class CommentCount(BaseModel):
    total: int