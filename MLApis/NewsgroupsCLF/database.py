#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pydantic import BaseModel


class PredictionInput(BaseModel):
    text: str


class PredictionOutput(BaseModel):
    category: str
