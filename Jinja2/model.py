#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Optional
from fastapi import Form
from pydantic import BaseModel


class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

    class Config:
        json_schema_extra = {
            'Example': {
                'item': 'example item 1',
                'description': 'Description for example 1',
            }
        }


class TodoItem(BaseModel):
    id: int
    status: str
    item: Todo

    class Config:
        json_schema_extra = {
            'Example_1': {
                'id': 1,
                'status': 'Published',
                'item': {
                    'item': 'example item 1',
                    'description': 'Description for example 1',
                }
            },

            'Example_2': {
                'id': 2,
                'status': 'Draft',
                'item': {
                    'item': 'example item 2',
                    'description': None,    # No description is given
                }
            }
        }
