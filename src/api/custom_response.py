#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.responses import (HTMLResponse, PlainTextResponse)
import uvicorn as uv

app = FastAPI(title="FastAPI development", version="0.1.0")


@app.get('/')
async def root() -> dict:
    return { "message": "Hello!" }


@app.get('/html', response_class=HTMLResponse)
async def get_html():
    return """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>FastAPI: Custom Response</title>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {
                        margin: 0;
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 
                                    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
                        font-size: 1.5em;
                        padding: 0.4em 0.8em;
                        background-color: powderblue;
                    }
                </style>
                <body>
                    <h1 style="color:teal;">StackML: ML question answering blog</h1>
                    <div>
                        <p>Q.1 What is Linear Regression</p>
                        <p>Linear Regression</p>
                        <p>Linear regression is a quiet and the simplest statistical regression method used 
                           for predictive analysis in machine learning. Linear regression shows the linear 
                           relationship between the independent(predictor) variable i.e. X-axis and the 
                           dependent(output) variable i.e. Y-axis, called linear regression.
                        </p>
                    </div>
                </body>
            </head>
        </html>
    """


@app.get('/text', response_class=PlainTextResponse)
async def text() -> str:
    return "Hello world!"


if __name__ == "__main__":
    uv.run('custom_response:app', reload=True)
