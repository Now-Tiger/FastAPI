#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI, Depends, Request, status, HTTPException
from fastapi.responses import JSONResponse
# from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestFormStrict
import uvicorn as uv

__version__ = '0.1.0'

app = FastAPI(
    title='Authentication', description="""# FastAPI Authentication using JWT""", version=__version__,
)

@app.get('/')
async def root(req: Request) -> JSONResponse:
    return JSONResponse(content={'Message': 'Successfully reached.'},  status_code=status.HTTP_200_OK)


if __name__ == '__main__':
    uv.run('main:app', reload=True)