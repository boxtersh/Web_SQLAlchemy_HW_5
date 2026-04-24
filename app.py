from fastapi import FastAPI

from models import Base
from databases import engine
from movies_router import movies_router


def run_app():
    Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(movies_router, prefix="/api")