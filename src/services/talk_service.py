from sqlalchemy.orm import Session
from src.models.talk import Talk
from src.models.user_talk import UserTalk
from src.schemas.talk_schema import CreateTalk, ResponseTalk, UpdateTalk
from src.schemas.user_talk_schema import CreateUserTalk
import time

class TalkService:
    def __init__(self, db: Session):
        self.db = db


    async def create_user_talk(self, userTalk: CreateUserTalk):
        talk = self.create_talk(userTalk.talk)
        for uuid in userTalk.uuids:
            new_user_talk = UserTalk(user_uuid = uuid, talk_id = talk.id)
            self.db.add(new_user_talk)
            self.db.commit()
            self.db.refresh(new_user_talk)
        return ResponseTalk(
             id=talk.id,
            title=talk.title,
            description=talk.description,
            url=talk.url,
            create_time=talk.create_time,
            timestamp=talk.timestamp
        )



    def create_talk(self, talk_data: CreateTalk) -> ResponseTalk:
        new_talk = Talk(
            title=talk_data.title,
            description=talk_data.description,
            url=talk_data.url,
            create_time=int(time.time()),
            timestamp=int(time.time()),
        )
        self.db.add(new_talk)
        self.db.commit()
        self.db.refresh(new_talk)
        return ResponseTalk(
            id=new_talk.id,
            title=new_talk.title,
            description=new_talk.description,
            url=new_talk.url,
            create_time=new_talk.create_time,
            timestamp=new_talk.timestamp
        )

    def get_talk(self, talk_id: str) -> ResponseTalk:
        talk = self.db.query(Talk).filter(Talk.id == talk_id).first()
        if not talk:
            raise ValueError("Talk not found")
        return ResponseTalk(
            id=talk.id,
            title=talk.title,
            description=talk.description,
            url=talk.url,
            create_time=talk.create_time,
            timestamp=talk.timestamp
        )
    
    def getTalks(self, skip: int = 0, limit: int = 50):
        talks = self.db.query(Talk).offset(skip).limit(limit).all()
        return [
            ResponseTalk(
                id=talk.id,
                title=talk.title,
                description=talk.description,
                url=talk.url,
                create_time=talk.create_time,
                timestamp=talk.timestamp
            ) for talk in talks
        ]   

    def update_talk(self, talk_data: UpdateTalk) -> ResponseTalk:
        talk = self.db.query(Talk).filter(Talk.id == talk_data.id).first()
        if not talk:
            raise ValueError("Talk not found")
        for key, value in talk_data.model_dump(exclude_unset=True).items():
            setattr(talk, key, value)
        self.db.commit()
        self.db.refresh(talk)
        return ResponseTalk(
            id=talk.id,
            title=talk.title,
            description=talk.description,
            url=talk.url,
            create_time=talk.create_time,
            timestamp=talk.timestamp
        )   
    