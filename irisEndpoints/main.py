#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import uvicorn as uv


app = FastAPI(
    title="Iris ML app endpoints",
    description="""# Fastapi backend apis f=of ML classification app""",
    version="0.1",
)


@app.get('/')
async def home(req: Request) -> JSONResponse:
    return {'Message': "Welcome back Neo"}


@app.get('/api/v1/predict')
async def predict(req: Request) -> JSONResponse:
    if not req:
        return HTTPException(status_code=401, detail=("Empty input message!"))
    return {"Message": "use model.predict here!"}


def main() -> None:
    uv.run('main:app', reload=True)
    return


if __name__ == '__main__':
    main()
