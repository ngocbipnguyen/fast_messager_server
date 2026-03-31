from fastapi import APIRouter, Depends
from src.db.session import get_db
from src.services.user_talk_service import UserTalkService
from src.schemas.user_talk_schema import ResponseUserTalk
from typing import List
from src.core.deps import get_current_user


route = APIRouter(prefix="/user_talk")

def getService(db=Depends(get_db)):
    return UserTalkService(db)

@route.get("/", response_model= List[ResponseUserTalk])
def getUserTalks(service: UserTalkService = Depends(getService), email: str = Depends(get_current_user))-> List[ResponseUserTalk]:
    return service.getUserTalk()

@route.get("/talk_id", response_model= List[ResponseUserTalk])
def getUserTalksByTalk(talk_id:str, service: UserTalkService = Depends(getService) , email: str = Depends(get_current_user))-> List[ResponseUserTalk]:
    return service.getUserTalkByTalk(talk_id=talk_id)
