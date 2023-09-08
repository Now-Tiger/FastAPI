#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
import uvicorn as uv

from todo import todo_router as router


app = FastAPI(
    title='📌 FastAPI Tutorial',
    description='''# Simple Todo Api''',
    version='0.0.1',
)

# * Implement welcome page route here using Jinja2 templating.

app.include_router(router=router)


if __name__ == '__main__':
    uv.run('main:app', reload=True,)
