#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn as uv


app = FastAPI(title="Response parameter")


class Item(BaseModel):
    id: int
    value: str


class Message(BaseModel):
    message: str


@app.get('/item/{item_id}', response_model=Item, responses={404: {'model':Message}})
async def read_item(item_id: int) -> JSONResponse:
    if item_id == 1:
        return {'id': 'foo', 'value': 'There goes my hero'}
    return JSONResponse(status_code=404, content={'message': 'Item not found'})


if __name__ == '__main__':
    uv.run('main:app', reload=True)
