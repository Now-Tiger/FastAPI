#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import (Depends, FastAPI)
import uvicorn as uv

from database import PredictionOutput
from predictionModel import NewsgroupModel


app = FastAPI()
newsgroup_model = NewsgroupModel()


@app.get("/")
async def root() -> dict:
    return { "message": "successful!" }


@app.post("/prediction")
async def prediction(
    output: PredictionOutput = Depends(newsgroup_model.predict),
    ) -> PredictionOutput:
    return output


@app.on_event("startup")
async def startup() -> None:
    newsgroup_model.load_model()


if __name__ == "__main__":
    uv.run("endpoint:app", reload=True)