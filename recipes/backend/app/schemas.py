from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional


class RecipeBase(BaseModel):
    cuisine: Optional[str] = None
    title: str
    rating: Optional[float] = Field(default=None)
    prep_time: Optional[int] = Field(default=None)
    cook_time: Optional[int] = Field(default=None)
    total_time: Optional[int] = Field(default=None)
    description: Optional[str] = None
    nutrients: Optional[dict[str, Any]] = None
    serves: Optional[str] = None


class RecipeOut(RecipeBase):
    id: int

    class Config:
        from_attributes = True
