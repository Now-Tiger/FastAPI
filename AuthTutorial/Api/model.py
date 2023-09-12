#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_name: str | None = None


class User(BaseModel):
    user_name: str | None = None
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(BaseModel):
    hashed_password: str
