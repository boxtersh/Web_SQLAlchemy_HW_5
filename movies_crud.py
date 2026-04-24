from sqlalchemy import select

from databases import SessionLocal
from models import Movie
from schemas import WatchStatusSet


def get_movies(db: SessionLocal, skip: int, limit: int, is_watched: bool) -> list[Movie]:
    query = select(Movie).offset(skip).limit(limit)
    if is_watched is not None:
        query = query.where(Movie.is_watched == is_watched)
    return db.execute(query).scalars().all()


def get_movie_by_id(db: SessionLocal, movie_id: int) -> Movie | None:
    is_movie = db.get(Movie, movie_id)
    if is_movie is None:
        return None
    return is_movie


def create_movie(db: SessionLocal, serialized_data: dict) -> Movie:
    movie = Movie(**serialized_data)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie


def update_movie_by_id(db: SessionLocal, movie_id: int, serialized_data: dict) -> Movie | None:
    is_movie = get_movie_by_id(db, movie_id)
    if is_movie is None:
        return None
    for attr, value in serialized_data.items():
        setattr(is_movie, attr, value)
    db.commit()
    db.refresh(is_movie)
    return is_movie


def delete_movie_by_id(db: SessionLocal, movie_id: int) -> bool:
    is_movie = get_movie_by_id(db, movie_id)
    if is_movie is None:
        return False
    db.delete(is_movie)
    db.commit()
    return True


def update_watch_status_movie_by_id(db: SessionLocal, movie_id: int, watch_status: WatchStatusSet) -> Movie | None:
    is_movie = get_movie_by_id(db, movie_id)
    if is_movie is None:
        return None
    if is_movie.is_watched == watch_status.is_watched:
        return is_movie
    is_movie.is_watched = watch_status.is_watched
    db.commit()
    db.refresh(is_movie)
    return is_movie


def reset_watch_status_movie_by_id(db: SessionLocal, movie_id: int) -> Movie | None:
    is_movie = get_movie_by_id(db, movie_id)
    if is_movie is None:
        return None
    if not is_movie.is_watched:
        return is_movie
    is_movie.is_watched = False
    db.commit()
    db.refresh(is_movie)
    return is_movie