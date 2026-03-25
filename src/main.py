from fastapi import FastAPI
from src.routers.talk_route import router as talk_router
from src.routers.user_route import router as user_router
from src.routers.message_route import route as message_route
from src.routers.login_route import route as login_route
from src.db.session import Base, engine
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(talk_router, prefix="/v1")
app.include_router(user_router, prefix="/v1")
app.include_router(message_route, prefix="/v1")
app.include_router(login_route, prefix="/v1")
