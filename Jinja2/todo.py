#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

from fastapi import Depends, Request
from fastapi import APIRouter, Path, status
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates

from model import Todo

__version__ = '0.0.1'

templates = Jinja2Templates(directory='templates')
todo_router = APIRouter()
todos = list()


@todo_router.get('/')
async def get_todos(req: Request):
    return templates.TemplateResponse("homepage.html", {
        "request": req,
        "message": "Succefully loaded.",
    })


@todo_router.get('/todos')
async def get_todos(req: Request):
    return templates.TemplateResponse("todo.html", {
        "request": req,
        "todos": todos,
    })


@todo_router.get('/todo/{todo_id}')
async def get_single_todo(
    req: Request, todo_id: int = Path(..., title='ID of the todo to retrive')):
    for todo in todos:
        if todo.id == todo_id:
            return templates.TemplateResponse("todo.html", {
                "request": req,
                "todo": todo,
            })
    return HTTPException(status_code=404, detail="Todo with the given ID does not exist")


@todo_router.post('/todo')
async def post_todo(req: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todos) + 1
    todos.append(todo)
    return templates.TemplateResponse("todo.html", {
        "request": req,
        "todos": todos,
    })
