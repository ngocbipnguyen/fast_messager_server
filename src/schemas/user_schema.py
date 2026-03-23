from pydantic import BaseModel
from typing import Optional

class CreateUser(BaseModel):
    username: str
    email: str
    password: str
    description: Optional[str]
    url_photo: Optional[str]


class ResponseUser(BaseModel):
    uuid: str
    username: str
    email: str
    description: Optional[str]
    url_photo: Optional[str]
    token: Optional[str]
    create_time: int
    update_time: int
    timestamp: int
    is_active: bool

class UpdateUser(BaseModel):
    uuid: str
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    description: Optional[str]
    url_photo: Optional[str]
    timestamp: Optional[int]
    is_active: Optional[bool]