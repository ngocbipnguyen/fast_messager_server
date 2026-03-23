from pydantic import BaseModel
from typing import Optional, List
from src.schemas.talk_schema import CreateTalk
class CreateUserTalk(BaseModel):
    user_uuid: str
    talk_id: str
    timestamp = Optional[int]
    uuids: List[str]
    talk: CreateTalk

