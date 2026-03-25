from pydantic import BaseModel

class ResponseLogin(BaseModel):
    uuid: str
    email: str
    access_token: str
    token_type: str = "bearer"