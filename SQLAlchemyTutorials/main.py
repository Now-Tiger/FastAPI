#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Optional, List, Dict
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn as uv
from datetime import datetime


app = FastAPI(title="Simple app", version="0.0.1")


class UserSchema(BaseModel):
    id: int
    name: Optional[str]
    username: str
    password: str
    tags: Optional[List[str]] = None

    class config:
        schema_extras = {
            "example": {
                "id": 1,
                "name": "Tiger",
                "username": "TigerHere",
                "password": "strongpassword",
                "tags": ["premium_user", "one_year_subscription"],
            }
        }

    def __repr__(self) -> str:
        return f"User Table (id = {self.id}, name = {self.name}, username = {self.username}) | time: {datetime.now()}"


user_one = UserSchema(
    id=1,
    name="Tiger",
    username="TigerHere",
    password="complexpassword",
    tags=["premium_user"],
)
user_two = UserSchema(
    id=2,
    name="Tom Holland",
    username="iamspidey",
    password="norizzholland",
    tags=["not_premium"],
)
user_three = UserSchema(
    id=3,
    name="John Cene",
    username="youcantseeme",
    password="champion",
)

userDB = [user_one, user_two, user_three]


@app.get("/", tags=["rootpage"])
async def home() -> Dict[str, str]:
    return {"message": "Home page!"}


@app.get("/api/v1/users")
async def users() -> Dict[str, list[UserSchema]]:
    return {"users": userDB}


@app.get("/api/v1/user/{userid}")
async def get_userby_id(userid: int) -> JSONResponse | None:
    for user in userDB:
        if user.id == userid:
            return JSONResponse(
                content={"user": user},
                status_code=status.HTTP_200_OK,
            )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not found",
        )


@app.post("/api/v1/register")
async def register(user: UserSchema) -> Dict:
    userDB.append(user)
    return {"message": "success", "users": userDB}


@app.post("/api/v1/create/user")
async def create_user(user: UserSchema) -> JSONResponse:
    try:
        id = user.id
        newUser = UserSchema(
            id=id,
            name=user.name,
            username=user.username,
            password=user.password,
        )
        return JSONResponse(
            content={
                "message": "success",
                "user": newUser,
            },
            status_code=status.HTTP_201_CREATED,
        )
    except Exception:
        return JSONResponse(
            content={
                "message": "internal server error",
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


if __name__ == "__main__":
    uv.run("main:app", reload=True, port=8080)
