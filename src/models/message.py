from src.db.session import Base
from sqlalchemy import Column, String, BigInteger, ForeignKey, Integer
from uuid import uuid4
from sqlalchemy.orm import relationship

class Message(Base):
    __tablename__ = "messages"


    id = Column(String, primary_key=True,default=lambda:str(uuid4()))
    content = Column(String, nullable=False)
    type = Column(Integer)
    motion = Column(Integer)
    timestamp = Column(BigInteger, default=0)
    
    from_user =  Column(String,ForeignKey("users.uuid"), nullable=False)
    from_talk = Column(String,ForeignKey("talks.id"), nullable=False)

    userMessage = relationship("User", back_populates="messages")
    talkMessage = relationship("Talk", back_populates="messages")
