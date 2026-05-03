from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

from schemas import MovieRead, MovieCreate, MovieUpdate, WatchStatusSet
from databases import get_db
import movies_crud as crud

movies_router = APIRouter()
templates = Jinja2Templates(directory="templates")

#1. Получить список фильмов
# @movies_router.get('/movies', response_model=list[MovieRead], status_code=200)
# def get_movies(skip: Annotated[int, Query(ge=0)] = 0,
#                limit: Annotated[int, Query(gt=0)] = 100,
#                is_watched: bool | None = None,
#                db: Session = Depends(get_db)):
#     lst_movies = crud.get_movies(db, skip, limit, is_watched)
#     return lst_movies
@movies_router.get('/movies', response_class=HTMLResponse)
async def get_movies(request: Request, skip: Annotated[int, Query(ge=0)] = 0,
               limit: Annotated[int, Query(gt=0)] = 100,
               is_watched: bool | None = None,
               db: Session = Depends(get_db)):
    lst_movies = crud.get_movies(db, skip, limit, is_watched)
    return templates.TemplateResponse(
        name="list_movies.html", request=request,
        context={
            "movies": lst_movies
        })



#2. Получить один фильм
@movies_router.get('/movies/{movie_id}', response_model=MovieRead, status_code=200)
async def get_movie_by_id(movie_id: Annotated[int, Path(gt=0)], db: Session = Depends(get_db)):
    is_movie = crud.get_movie_by_id(db, movie_id)
    if is_movie is None:
        raise HTTPException(status_code=404)
    return is_movie


#3. Создать фильм
@movies_router.post('/movies', response_model=MovieRead, status_code=201)
async def create_movie(movie_create: MovieCreate, db: Session = Depends(get_db)):
    serialized_data = movie_create.model_dump()
    movie_read = crud.create_movie(db, serialized_data)
    return movie_read


#4. Обновить фильм
@movies_router.put('/movies/{movie_id}', response_model=MovieRead, status_code=200)
async def update_movie_by_id(movie_update: MovieUpdate, movie_id: Annotated[int,
                        Path(gt=0)], db: Session = Depends(get_db)):
    serialized_data = movie_update.model_dump(exclude_unset=True)
    is_movie = crud.update_movie_by_id(db, movie_id, serialized_data)
    if is_movie is None:
        raise HTTPException(status_code=404)
    return is_movie


#5. Удалить фильм
@movies_router.delete('/movies/{movie_id}', status_code=204)
async def delete_movie_by_id(movie_id: Annotated[int, Path(gt=0)], db: Session = Depends(get_db)) -> None:
    is_movie = crud.delete_movie_by_id(db, movie_id)
    if not is_movie:
        raise HTTPException(status_code=404)
    return None


#6. Пометить фильм как просмотренный или непросмотренный
@movies_router.patch('/movies/{movie_id}', response_model=MovieRead, status_code=200)
async def update_watch_status_movie_by_id(movie_id: Annotated[int, Path(gt=0)], watch_status: WatchStatusSet,
                       db: Session = Depends(get_db)):
    is_movie = crud.update_watch_status_movie_by_id(db, movie_id, watch_status)
    if is_movie is None:
        raise HTTPException(status_code=404)
    return is_movie


#7. Снять признак просмотра
@movies_router.patch('/movies/reset_watched/{movie_id}/', response_model=MovieRead, status_code=200)
async def reset_watch_status_movie_by_id(movie_id: Annotated[int, Path(gt=0)], db: Session = Depends(get_db)):
    is_movie = crud.reset_watch_status_movie_by_id(db, movie_id)
    if is_movie is None:
        raise HTTPException(status_code=404)
    return is_movie