#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import joblib
from typing import Optional

from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from sklearn.pipeline import Pipeline


class PredictionInput(BaseModel):
    text: str

    def __len__(self) -> int:
        return len(self.text)


class PredictionOutput(BaseModel):
    language: str
    

class LanguageDetectionModel:
    """ 
    Loads model and Makes prediction
    """
    model: Optional[Pipeline]
    targets: Optional[list[str]]

    def load_model(self) -> None:
        """ Load the model """
        model_file = os.path.join(os.path.dirname(__file__), 'langDetTrained1.joblib')
        loaded_model: tuple[Pipeline, list[str]] = joblib.load(model_file)
        model, targets = loaded_model
        self._model = model
        self._targets = targets

    async def predict(self, input: PredictionInput) -> PredictionOutput:
        """ Runs a prediction.
            * if input is empty raise an HTTP 404 error
            * else run prediction
        """
        if len(input) <= 1:
            raise HTTPException(status_code=404, detail="Empty input string provided.")
        
        predictions = self._model.predict([input.text])
        language = self._targets[predictions[0]]
        return PredictionOutput(language=language)