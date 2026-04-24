from datetime import datetime
from sqlalchemy import String, func
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)
class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    genre: Mapped[str] = mapped_column(String(256))
    release_year: Mapped[int]
    is_watched: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now())

