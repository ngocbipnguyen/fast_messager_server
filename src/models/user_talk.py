from src.db.session import Base
from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, Table
from uuid import uuid4
from sqlalchemy.orm import relationship
from uuid import uuid4
class UserTalk(Base):
    __tablename__ = "user_talks"

    id = Column(String, primary_key=True, default= lambda: f"user_talk_{uuid4().hex[:12]}")
    user_uuid = Column(String,ForeignKey("users.uuid"), nullable=False)
    talk_id = Column(String,ForeignKey("talks.id"), nullable=False)
    user = relationship("User", back_populates="talks")
    talk = relationship("Talk", back_populates="user")

