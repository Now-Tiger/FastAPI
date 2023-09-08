#!/usr/bin/env python3
# -*- coding: utf -*-
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    views: Optional[int]
    review: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Example title",
                "views": 77,
                "review": "Example review",
            }
        }
