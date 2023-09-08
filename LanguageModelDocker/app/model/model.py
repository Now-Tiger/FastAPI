#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import string
import pickle
from pathlib import Path
from pydantic import BaseModel

from sklearn.feature_extraction.text import CountVectorizer


__version__ = '0.1.0'

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/train_model_pipeline-{__version__}.pkl", "rb") as file:
    model = pickle.load(file=file)

classes = [
    'Arabic',
    'Danish',
    'Dutch',
    'English',
    'French',
    'German',
    'Greek',
    'Hindi',
    'Italian',
    'Kannada',
    'Malayalam',
    'Portugeese',
    'Russian',
    'Spanish',
    'Sweedish',
    'Tamil',
    'Turkish',
]


class PredictionInput(BaseModel):
    text: str

    def __repr__(self) -> str:
        return f"input: [ {self.text} ]"
    

class PredictionOut(BaseModel):
    language: str

    def __repr__(self) -> str:
        return f"prediction: [ {self.language} ]"


def predict_pipeline(input: PredictionInput) -> None:
    vec = CountVectorizer(lowercase=True)
    transformed = vec.fit_transform([input])
    pred = model.predict(transformed)
    return classes[pred[0]]

if __name__ == '__main__':
    res = predict_pipeline("Hello")
    print(res)

    """FIX THIS ERROR 
            res = predict_pipeline("Hello")
          ^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/Users/a1/Documents/FastAPI/LanguageModelDocker/app/model/model.py", line 61, in predict_pipeline
            pred = model.predict([input.text])
    """

    #? FIXED ISSUE: First convert the input text into the a numerical vectorized form.
    # * Then make predictions -> basically convert text into the numerical vector.
    # * Fix is not yet implemented, refer to the language detection notebook on kaggle.