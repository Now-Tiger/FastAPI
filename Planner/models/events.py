#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List
from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "GenAI Fundamentals Microsoft",
                "image": "some/path/to/the/url",
                "description": "Microsoft developers will teach fundamentals of Generative AI and its applications using Azure and OpenAI",
                "tags": ["python", "generative-ai", "openai", "machine-learning"],
                "location": "Google Meet",
            }
        }
