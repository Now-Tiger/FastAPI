#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
from routes.users import userRouter
from routes.events import eventRouter
import uvicorn as uv


app = FastAPI(
    title="Planner API ✅",
    description="""<h2>Events Planner Application</h2>""",
    version="0.0.1",
)

# Register routes
app.include_router(userRouter, prefix="/user")
app.include_router(eventRouter, prefix="/event")


@app.get("/")
async def root() -> dict[str, str]:
    return {"Message": "Home Page of Planner"}


if __name__ == "__main__":
    uv.run("main:app", reload=True, port=8080)
