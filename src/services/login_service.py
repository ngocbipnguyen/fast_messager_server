from fastapi import Depends, status
from src.core.jwt_token import get_password_hash, verify_password, create_access_token
from src.models.user import User
from sqlalchemy.orm import Session
from http.client import HTTPException
from src.schemas.login_schema import ResponseLogin

from datetime import timedelta
class LoginService:
    def __init__(self, db: Session):
        self.db = db
    
    def login(self, email: str, password: str):
        user = self.authenticate_user(email=email, password=password)
        if not user:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"}, 
            )
        access_token_expires = timedelta(minutes=15)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        # user.token = access_token
        # if user:
        #     for key, value in user.model_dump(exclude_unset=True).items():
        #         setattr(user, key, value)
        #     self.db.commit()
        #     self.db.refresh(user)
        return ResponseLogin(uuid=user.uuid, email= user.email, access_token=access_token)


    
    def authenticate_user(self, email: str, password: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            return False
        if not verify_password(password, user.password):
            return False
        return user