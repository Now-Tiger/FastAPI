#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI
import uvicorn as uv

from todo import todo_router as router


app = FastAPI(
    title='FastAPI Tutorial',
    description='''# Simple Todo Api''',
    version='0.0.1',
)


@app.get('/')
async def welcome() -> dict:
    return {'Message': 'Welcome back Neo!'}


app.include_router(router=router)


def main() -> None:
    uv.run('main:app', reload=True,)
    return


if __name__ == '__main__':
    main()
