from datetime import datetime, date
from typing import Annotated

from pydantic import BaseModel, Field, AfterValidator, ConfigDict

from constants import const


def validate_range_year(year: int) -> int:
    current_year = date.today().year
    if not (const.RANGE_YEAR_BEGIN <= year <= current_year):
        raise ValueError(f'Год выпуска должен быть в диапазоне 1880–{current_year}')
    return year


class MovieCreate(BaseModel):
    title: str = Field(..., min_length=const.TITLE_MIN, max_length=const.TITLE_MAX)
    genre: str = Field(..., min_length=const.GENRE_MIN, max_length=const.GENRE_MAX)
    release_year: Annotated[int, AfterValidator(validate_range_year)]


class MovieUpdate(BaseModel):
    title: str | None
    genre: str | None
    release_year: Annotated[int | None, AfterValidator(validate_range_year)]


class WatchStatusSet(BaseModel):
    is_watched: bool = False


class MovieRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    genre: str
    release_year: int
    is_watched: bool
    created_at: datetime