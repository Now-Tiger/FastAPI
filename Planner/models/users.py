#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "example@somemail.com",
                "password": "strongpassword!!!",
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "example@somemail.com",
                "password": "strongpassword!!!",
            }
        }
