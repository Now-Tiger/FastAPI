#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn as uv

# ?FIX BELOW ERRORS WHEN IMPORTING FUNCTIONS FROM FOLDERS
# from app.model.model import predict_pipeline
# from app.model.model import __version__ as model_version


app = FastAPI(title='NLP EndPoint', version='0.1.0')


@app.get('/')
async def checkup(req: Request) -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content={'message': "OK", 'Model -V': '0.1.0'}
    )


if __name__ == '__main__':
    uv.run('main:app', reload=True,)
