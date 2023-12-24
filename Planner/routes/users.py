#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter, status, HTTPException
from models.users import User, UserSignIn


users = {}
userRouter = APIRouter(tags=["User"])


@userRouter.post("/signup")
async def user_sign_up(data: User) -> dict[str, str]:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists",
        )
    users[data.email] = data
    return {"Message": "User successfully registered"}


@userRouter.post("/signin")
async def user_sign_in(data: UserSignIn) -> dict[str, str]:
    if data.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist"
        )
    if users[data.email].password != data.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credential passed"
        )
    return {"Message": "User signed in successfully"}
