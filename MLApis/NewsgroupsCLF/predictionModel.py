#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import joblib
from typing import Optional

from sklearn.pipeline import Pipeline
from database import (PredictionInput, PredictionOutput)


class NewsgroupModel:
    """ 
    Loads model and Makes prediction
    """
    model: Optional[Pipeline]
    targets: Optional[list[str]]

    def load_model(self) -> None:
        """ Load the model """
        model_file = os.path.join(
            os.path.dirname(__file__),
            'newsgroups_model.joblib'
        )
        loaded_model: tuple[Pipeline, list[str]] = joblib.load(model_file)
        model, targets = loaded_model
        self._model = model
        self._targets = targets

    async def predict(self, input: PredictionInput) -> PredictionOutput:
        """ Runs a prediction """
        # if not self.model or self.targets:
        #     raise RuntimeError("Model is not loaded")
        # ?FIX THE ABOVE BUG. GIVES MODEL IS NOT LOADED. RUNTIME ERROR

        predictions = self._model.predict([input.text])
        category = self._targets[predictions[0]]
        return PredictionOutput(category=category)
