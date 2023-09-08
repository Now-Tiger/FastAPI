#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn as uv

from todo import todo_router as router


app = FastAPI(
    title="Todo API",
    description="""# FastAPI Developement""",
    version="0.0.1"
)


@app.get('/')
async def welcome() -> JSONResponse:
    return JSONResponse(content={ "message": "Welcome back Neo!" }, status_code=200)


app.include_router(router=router)


if __name__ == '__main__':
    uv.run("main:app", reload=True)
