from fastapi import APIRouter, Depends
from src.core.deps import get_current_user
from src.services.talk_service import TalkService
from src.schemas.talk_schema import CreateTalk, ResponseTalk, UpdateTalk, CreateTalks
from src.schemas.user_talk_schema import CreateUserTalk
from src.db.session import get_db

router = APIRouter(prefix="/talks")

def getService(db=Depends(get_db)):
    return TalkService(db)

@router.post("/", response_model=ResponseTalk)
def create_talk(talk_data: CreateTalk, service: TalkService = Depends(getService), email: str = Depends(get_current_user)):
    return service.create_talk(talk_data)

@router.post("/create_talks", response_model=ResponseTalk)
async def create_talk_user(user_talk: CreateTalks, service: TalkService = Depends(getService), email: str = Depends(get_current_user)):
    return await service.create_talks(create_talks=user_talk)


@router.get("/{talk_id}", response_model=ResponseTalk)
def get_talk(talk_id: str, service: TalkService = Depends(getService)):
    return service.get_talk(talk_id)

@router.put("/{talk_id}", response_model=ResponseTalk)
def update_talk(talk_id: str, talk_data: UpdateTalk, service: TalkService = Depends(getService)):
    return service.update_talk(talk_id, talk_data)

@router.get("/", response_model=list[ResponseTalk])
def get_talks(skip: int = 0, limit: int = 50, service: TalkService = Depends(getService)):
    return service.getTalks(skip, limit)

