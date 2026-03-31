from pydantic import BaseModel

class CreateMessage(BaseModel):
    content : str
    type : int
    motion : int
    from_user : str
    from_talk : str

class MessageParams(BaseModel):
    from_talk : str = None
    from_user : str = None
    limit : int = 50
    skip : int = 0

class ResponseMessage(BaseModel):
    id : str
    content : str
    type : int
    motion : int
    timestamp : int
    from_user : str
    from_talk : str

class UpdateMessage(BaseModel):
    id : str
    content : str
    type : int
    motion : int

