from src.db.session import Base
from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, Table
from uuid import uuid4
from sqlalchemy.orm import relationship
class UserTalk(Base):
    __tablename__ = "user_talks"

    user_uuid = Column(String,ForeignKey("users.uuid"), nullable=False)
    talk_id = Column(String,ForeignKey("talks.id"), nullable=False)
    user = relationship("User", back_populates="user_talks")
    talk = relationship("Talk", back_populates="user_talks")

