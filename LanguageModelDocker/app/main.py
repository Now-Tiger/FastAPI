#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn as uv

# from app.model.model import predict_pipeline
# from app.model.model import __version__
from model.model import predict_pipeline
from model.model import __version__

# ?FIX BELOW ERRORS WHEN IMPORTING FUNCTIONS FROM FOLDERS
# from app.model.model import predict_pipeline
# from app.model.model import __version__ as model_version


app = FastAPI(title='NLP EndPoint', version=__version__)


class TextIn(BaseModel):
    text: str


class PredictionOutput(BaseModel):
    language: str


@app.get('/')
async def checkup(req: Request) -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content={'message': "Hello",}
    )

@app.post('/api/v1/predict-lang', response_model=PredictionOutput)
async def predict(req: Request, payload: TextIn) -> JSONResponse:
    if not payload.text:
        raise HTTPException(status_code=404, detail=("Empty input string"))
    language = predict_pipeline(payload.text)
    return { "language": language }



if __name__ == '__main__':
    uv.run('main:app', reload=True,)
