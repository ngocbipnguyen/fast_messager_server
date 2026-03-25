from src.db.session import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter
from src.schemas.login_schema import ResponseLogin
from typing import Annotated
from src.services.login_service import LoginService

route = APIRouter(prefix="/login")

@route.post("/", response_model=ResponseLogin)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db = Depends(get_db))-> ResponseLogin:
    service = LoginService(db=db)
    return service.login(form_data.username, form_data.password)