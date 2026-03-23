from src.db.session import Base
from sqlalchemy import Column, Integer, String, BigInteger
from uuid import uuid4
from sqlalchemy.orm import relationship
class Talk(Base):
    __tablename__ = "talks"

    id = Column(String, primary_key=True,default= lambda: f"talk_{uuid4().hex[:12]}")
    title = Column(String, nullable=False)
    description = Column(String)
    create_time = Column(BigInteger)
    timestamp = Column(BigInteger)
    url = Column(String)
    content = Column(String)
    type = Column(Integer)

    user = relationship(
        "UserTalk",
        back_populates="talk"
    )
