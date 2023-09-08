#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse

from model import TodoItem
from fastapi.templating import Jinja2Templates


todo_router = APIRouter()
todos = list()

templates = Jinja2Templates(directory='templates/')


@todo_router.get('/todos')
async def retrive_todos() -> JSONResponse:
    if len(todos) < 1 or todos is None:
        return { 'Message': 'Add todo items first' }
    return { 'Todos': todos }


@todo_router.get('/todo/{todo_id}')
async def single_todo(todo_id: int = Path(..., title="The ID of todo to retrive")) -> JSONResponse:
    for todo in todos:
        if todo.id == todo_id:
            return {'Todo': todo}

    return {'Message': 'Todo with given ID does not exist.'}


@todo_router.post('/todo')
async def post_todo(todo: TodoItem) -> JSONResponse:
    if todo is None:
        return {'Message': 'Empty todo added'}
    else:
        todos.append(todo)
        return {'Message': 'Todo added sucessfully!'}


@todo_router.put('/todo/{todo_id}',)
async def update_todo(todo_id: int, todo_data: TodoItem) -> JSONResponse:
    for todo in todos:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {'Message': 'Updated todo successfully'}
        raise HTTPException(
            status_code=404, detail='Todo with given id does not exist')


@todo_router.delete('/todo/{todo_id}')
async def delete(todo_id: int = Path(..., title="id of the todo item to delete")) -> JSONResponse:
    for idx in range(len(todos)):
        todo = todos[idx]
        if todo.id == todo_id:
            todos.pop(idx)
            return { 'Message': 'Todo with given ID successfully deleted' }
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo with given id does not exists.")
    