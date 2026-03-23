from pydantic import BaseModel
from typing import Optional
class CreateTalk(BaseModel):
    title: str
    description: Optional[str]
    url: Optional[str]

class ResponseTalk(BaseModel):
    id: str
    title: str
    description: Optional[str]
    create_time: int
    timestamp: int
    url: str
    content: str
    type: int

class UpdateTalk(BaseModel):
    id: str
    title: Optional[str]
    description: Optional[str]
    url: Optional[str]
    content: Optional[str]
    type: Optional[int]
    timestamp: Optional[int]