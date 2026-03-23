from fastapi import FastAPI
from src.routers.talk_route import router as talk_router
from src.routers.user_route import router as user_router
from src.db.session import Base, engine
app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(talk_router, prefix="/v1")
app.include_router(user_router, prefix="/v1")
