from src.db.session import Base
from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from uuid import uuid4
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "users"

    uuid = Column(String, primary_key=True, default=lambda:str(uuid4()))
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    description = Column(String)
    url_photo = Column(String)
    token = Column(String)
    create_time = Column(BigInteger)
    update_time = Column(BigInteger)
    timestamp = Column(BigInteger)
    is_active = Column(Boolean, default=False)

    talks = relationship(
        "UserTalk",
        back_populates="user"
    )
    
    messages = relationship("Message", back_populates="userMessage")


