from sqlalchemy.orm import Session
from src.db.session import get_db
from fastapi import Depends, APIRouter
from src.services.message_service import MessageService
from src.schemas.message_schema import CreateMessage, ResponseMessage, UpdateMessage
from typing import List
from src.core.deps import get_current_user

route = APIRouter(prefix="/messages")

def getService(db=Depends(get_db)):
    return MessageService(db)

@route.post("/", response_model= ResponseMessage)
def createMessage(message: CreateMessage, service: MessageService = Depends(getService),email: str = Depends(get_current_user))-> ResponseMessage:
    return service.create_messsage(message)

@route.get("/", response_model=ResponseMessage) 
def getMessageByTalk(id: str,  service: MessageService = Depends(getService),email: str = Depends(get_current_user))-> List[ResponseMessage]:
    return service.getMessagesByTalk(talk_id=id)

@route.put("/update", response_model=ResponseMessage)
def updateMessage(data: UpdateMessage, service: MessageService = Depends(getService),email: str = Depends(get_current_user))-> ResponseMessage:
    return service.updateMessage(data=data)