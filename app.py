from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.templating import Jinja2Templates

from models import Base
from databases import engine
from routers.movies_router import movies_router


def run_app():
    Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.include_router(movies_router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get('/create_movie')
async def create_movie(request: Request):
    return templates.TemplateResponse(request=request, name="create_movie.html")


@app.get('/request_parameters')
async def create_movie(request: Request):
    return templates.TemplateResponse(request=request, name="request_parameters.html")