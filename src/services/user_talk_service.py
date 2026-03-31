from sqlalchemy.orm import Session
from typing import List
from src.schemas.user_talk_schema import ResponseUserTalk
from src.models.user_talk import UserTalk
class UserTalkService:

    def __init__(self, db : Session):
        self.db = db

    def getUserTalk(self)-> List[ResponseUserTalk]:
        user_talks = self.db.query(UserTalk).all()
        return [ResponseUserTalk(
                id= user_talk.id,
                user_uuid = user_talk.user_uuid,
                talk_id = user_talk.talk_id
            ) for user_talk in user_talks
        ]
    
    
    def getUserTalkByTalk(self, talk_id : str) -> List[ResponseUserTalk]:
        user_talks = self.db.query(UserTalk).filter(UserTalk.talk_id ==  talk_id).all()
        return [ResponseUserTalk(
                id= user_talk.id,
                user_uuid = user_talk.user_uuid,
                talk_id = user_talk.talk_id
            ) for user_talk in user_talks
        ]
