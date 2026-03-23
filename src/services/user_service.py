from sqlalchemy.orm import Session
from src.core.jwt_token import get_password_hash
import time
from src.models.user import User
from src.schemas.user_schema import CreateUser, ResponseUser, UpdateUser
from typing import List

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: CreateUser) -> ResponseUser:
        hashed_password = get_password_hash(user_data.password)
        user = User(
            username=user_data.username,
            email=user_data.email,
            password=hashed_password,
            description=user_data.description,
            url_photo=user_data.url_photo,
            create_time=int(time.time()),
            update_time=int(time.time()),
            timestamp=int(time.time()),
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return ResponseUser(
            uuid=user.uuid,
            username=user.username,
            email=user.email,
            description=user.description,
            url_photo=user.url_photo,
            token=user.token,
            create_time=user.create_time,
            update_time=user.update_time,
            timestamp=user.timestamp,
            is_active=user.is_active
        )

    def get_user(self, user_id: str):
        user =  self.db.query(User).filter(User.uuid == user_id).first() 
        if user:
            return ResponseUser(
                uuid=user.uuid,
                username=user.username,
                email=user.email,
                description=user.description,
                url_photo=user.url_photo,
                token=user.token,
                create_time=user.create_time,
                update_time=user.update_time,
                timestamp=user.timestamp,
                is_active=user.is_active
            )
        return None
    
    def getUsers(self, skip: int = 0, limit: int = 50)-> List[ResponseUser]:
        users = self.db.query(User).offset(skip).limit(limit).all()
        return [
            ResponseUser(
                uuid=user.uuid,
                username=user.username,
                email=user.email,
                description=user.description,
                url_photo=user.url_photo,
                token=user.token,
                create_time=user.create_time,
                update_time=user.update_time,
                timestamp=user.timestamp,
                is_active=user.is_active
            ) for user in users
        ]

    def update_user(self, data: UpdateUser):
        user = self.db.query(User).filter(User.uuid == data.uuid).first()
        if user:
            for key, value in data.model_dump(exclude_unset=True).items():
                setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
            return ResponseUser(
                uuid=user.uuid,
                username=user.username,
                email=user.email,
                description=user.description,
                url_photo=user.url_photo,
                token=user.token,
                create_time=user.create_time,
                update_time=user.update_time,
                timestamp=user.timestamp,
                is_active=user.is_active
            )
        return None
