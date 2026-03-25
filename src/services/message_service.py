from sqlalchemy.orm import Session
from src.models.message import Message
from src.schemas.message_schema import CreateMessage, UpdateMessage, ResponseMessage 
import time

class MessageService:

    def __init__(self, db: Session):
        self.db = db
    
    def create_messsage(self, user: CreateMessage):
        message = Message(content = user.content,
                                    type = user.type, 
                                    motion = user.motion, 
                                    from_user = user.from_user, 
                                    from_talk =  user.from_talk,
                                    timestamp = int(time.time()))
        user = self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return ResponseMessage(
            id =  message.id,
            content = message.content,
            type =  message.type,
            motion= message.motion,
            timestamp= message.timestamp,
            from_user= message.from_user,
            from_talk= message.from_talk
        )
    
    def getMessagesByTalk(self,talk_id: str, skip: int = 0, limit: int = 50):
        messages = self.db.query(Message).filter(Message.from_talk == talk_id).offset(skip).limit(limit).all()
        return [
            ResponseMessage(
                id =  message.id,
                content = message.content,
                type =  message.type,
                motion= message.motion,
                timestamp= message.timestamp,
                from_user= message.from_user,
                from_talk= message.from_talk
            ) for message in messages
        ]
    
    def updateMessage(self, data: UpdateMessage):
        message = self.db.query(Message).filter(Message.id == data.id).first()
        if message: 
            for key, value in data.model_dump(exclude_unset=True).items():
                    setattr(message, key, value)
        self.db.commit()
        self.db.refresh(message)
        return ResponseMessage(
            id =  message.id,
            content = message.content,
            type =  message.type,
            motion= message.motion,
            timestamp= message.timestamp,
            from_user= message.from_user,
            from_talk= message.from_talk
        )
    
    


        


