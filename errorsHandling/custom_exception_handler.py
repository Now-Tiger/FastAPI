#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn as uv


app = FastAPI()


class UnicornException(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exeption_handler(
    request: Request, exec: UnicornException
) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"message": f"Oops! {exec.name} did something! Fall back"},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str) -> JSONResponse:
    if name.lower() == "yolo":
        raise UnicornException(name=name)
    return {"Unicron name": name}


@app.get("/")
async def welcome() -> JSONResponse:
    return {"MSG": "Hello"}


if __name__ == "__main__":
    uv.run(
        "custom_exception_handler:app",
        reload=True,
        port=8000,
    )

