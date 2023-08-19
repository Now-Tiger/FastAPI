#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI, status, HTTPException
import uvicorn as uv


app = FastAPI()


small_db = { 'foo': 'The foo wrestlers' }


@app.get('/items/{item_id}')
async def get_item(item_id: str) -> dict:
    if item_id not in small_db:
        raise HTTPException(
            status_code=404, # or status.HTTP_404_NOT_FOUND <- better than hard coding
            detail="Item not found!",
            headers={"X-Error": "There goes my hero."}
        )
    return { 'item': small_db[item_id] }


if __name__ == '__main__':
    uv.run('httpExceptions:app', reload=True)