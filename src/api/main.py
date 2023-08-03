#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
import uvicorn as uv

app = FastAPI(title="FastAPI development", version="0.1.0")


@app.get('/')
async def root() -> dict:
    return { 'message': 'successful submission' }


if __name__ == "__main__":
    uv.run('main:app', reload=True, port=8080)