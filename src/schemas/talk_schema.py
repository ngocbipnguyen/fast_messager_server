from pydantic import BaseModel
from typing import Optional, List
class CreateTalk(BaseModel):
    title: str
    description: Optional[str]
    url: Optional[str]

class CreateTalks(BaseModel):
    title: str
    description: Optional[str] = None
    url: Optional[str] = None
    uuids: List[str]

class ResponseTalk(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    create_time: int
    timestamp: int
    url: Optional[str] = None

class UpdateTalk(BaseModel):
    id: str
    title: Optional[str]
    description: Optional[str]
    url: Optional[str]
    timestamp: Optional[int]