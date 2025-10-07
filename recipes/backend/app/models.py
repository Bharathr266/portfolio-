from __future__ import annotations

from sqlalchemy import Integer, String, Float, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import JSON

from .database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    cuisine: Mapped[str | None] = mapped_column(String(255), index=True)
    title: Mapped[str] = mapped_column(String(512), index=True)
    rating: Mapped[float | None] = mapped_column(Float, index=True)
    prep_time: Mapped[int | None] = mapped_column(Integer)
    cook_time: Mapped[int | None] = mapped_column(Integer)
    total_time: Mapped[int | None] = mapped_column(Integer, index=True)
    description: Mapped[str | None] = mapped_column(Text)
    nutrients: Mapped[dict | None] = mapped_column(JSON)
    serves: Mapped[str | None] = mapped_column(String(128))
