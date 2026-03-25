from fastapi import APIRouter, Depends
from src.core.deps import get_current_user
from src.services.user_service import UserService
from src.schemas.user_schema import CreateUser, ResponseUser, UpdateUser
from src.db.session import get_db
from typing import List
router = APIRouter(prefix="/users")

def getService(db=Depends(get_db)):
    return UserService(db)

@router.post("/", response_model=ResponseUser)
def create_user(user_data: CreateUser, service: UserService = Depends(getService)):
    return service.create_user(user_data)

@router.get("/",response_model=List[ResponseUser])
def getUsers(service: UserService = Depends(getService), email: str = Depends(get_current_user)):
    return service.getUsers()


@router.get("/{uuid}", response_model=ResponseUser)
def getUser(uuid:str, service: UserService = Depends(getService), email: str = Depends(get_current_user)):
    return service.get_user(user_id=uuid)

@router.put("/", response_model=ResponseUser)
def updateUser(data: UpdateUser ,service: UserService = Depends(getService), email: str = Depends(get_current_user)):
    return service.update_user(data=data)