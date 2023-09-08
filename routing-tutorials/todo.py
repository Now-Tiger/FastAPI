#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from model import Todo, Message

todo_router = APIRouter()

todos = list()


@todo_router.get("/todos")
async def retrive_todos() -> JSONResponse:
    return {'todos': todos}


@todo_router.get("/todo/{todo_id}", responses={404: {'Message': Message}})
async def get_single_todo(todo_id: int = Path(..., title="id of todo to retrive")) -> dict:
    for todo in todos:
        if todo.id == todo_id:
            return {'Todo': todo}
    return JSONResponse(status_code=404, content={'message': 'Todo with given ID does not exist.'})


@todo_router.post("/todo")
async def post_single_todo(todo: Todo) -> JSONResponse:
    if not todo:
        return JSONResponse(
            ontent={'Message': 'Provided empty information'}, status_code=422,
        )
    else:
        todos.append(todo)
        return JSONResponse(
            content={'message': 'Todo added successfully'}, status_code=200
        )
