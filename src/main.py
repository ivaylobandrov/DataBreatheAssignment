from fastapi import FastAPI
from src.routes import router
from src.config import engine
from src import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
