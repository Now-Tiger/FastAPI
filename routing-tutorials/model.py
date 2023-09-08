#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Optional
from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Item(BaseModel):
    item: str
    views: int
    status: Optional[str]

    class Config:
        json_schema_extra = {
            "Example": {
                "item": "Example item 1",
                "views": 77,
                "satus": "Published",
            }
        }


class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        json_schema_extra = {
            "id": 1,
            "item": {
                "item": "Inherited item 1 from Item class",
                "views": 77,        # Inherited from Item class views example
                "status": "Published"
            },

            "id": 2,
            "item": {
                "item": "Example item 2",
                "views": 55,
                "status": None      # This is a optional parameter/value
            }
        }
