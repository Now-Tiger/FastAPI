#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pydantic import BaseModel


class PredictionInput(BaseModel):
    text: str

    def __len__(self) -> int:
        return len(self.text)


class PredictionOutput(BaseModel):
    language: str
