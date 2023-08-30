#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import (Depends, FastAPI)
from fastapi.responses import JSONResponse
import uvicorn as uv

from model import LanguageDetectionModel, PredictionOutput

__version__ = '0.1.1'

app = FastAPI(
    title="ML Endpoint 🤸🏻‍♀️",
    description="""# ML Endpoint using FastAPI and ScikitLearn""",
    version=__version__
)
language_model = LanguageDetectionModel()


@app.get("/")
async def root() -> JSONResponse:
    return { "Message": "Successful! Try `http://localhost:8000/api/v1/prediction`" }


@app.post("/api/v1/prediction")
async def prediction(
    output: PredictionOutput = Depends(language_model.predict)) -> PredictionOutput:
    return output


@app.on_event("startup")
async def startup() -> None:
    language_model.load_model()


if __name__ == "__main__":
    uv.run("main:app", reload=True)