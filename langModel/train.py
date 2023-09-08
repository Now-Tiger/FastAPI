#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import string
import joblib

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, f1_score
from sklearn.pipeline import make_pipeline

from sklearn.model_selection import train_test_split as split

from warnings import filterwarnings
filterwarnings('ignore')


class Train(object):
    def __init__(self, inputs: np.ndarray, targets: np.ndarray) -> None:
        self._inputs  = inputs
        self._targets = targets
    
    def preprocess(self) -> list[str]:
        # Proper text processing is required stopwords removals, etc.
        table = list()
        for txt in self._inputs:
            txt = re.sub(r'[!@#$(),\n"%^*?\:;`0-9]', ' ', txt)
            txt = re.sub('https?://\S+|www\.\S+', '', txt)
            txt = re.sub('[%s]' % re.escape(string.punctuation), '', txt)
            txt = re.sub(r"^\s+|\s+$", "", txt)
            txt = re.sub(r'[^\w\s]', '', txt)
            txt = re.sub('<.*?>+', '', txt)
            txt = re.sub(' +', ' ', txt)
            txt = re.sub(r'[[]]', ' ', txt)
            txt = txt.lower()
            table.append(txt)
        return table

    def label_encode(self) -> tuple[np.ndarray, np.ndarray]:
        encoder = LabelEncoder().fit(self._targets)
        transformed = encoder.transform(self._targets)
        return transformed, encoder.classes_
    
    def vectorize(self, inputs: list[str]) -> list[np.float64]:
        vec = TfidfVectorizer(max_features=1000, lowercase=True, )
        transformed = vec.fit_transform(inputs).toarray()
        return transformed
    
    def accuracy(self, preds: np.ndarray, trues: np.ndarray) -> np.float64:
        f1_acc = f1_score(preds, trues, average='weighted')
        return f1_acc
    
    def build(self, inputs: np.ndarray, targets: np.ndarray) -> object:
        model = MultinomialNB().fit(inputs, targets)
        return model
        
    def pipeline_predict(self, inputs: list, targets: np.ndarray) -> tuple[object, np.ndarray, np.float64]:
        model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        model.fit(inputs, targets)
        preds = model.predict(inputs)
        accuracy = accuracy_score(preds, self._targets)
        return (model, preds, accuracy)
        

def main() -> None:
    raw = pd.read_csv('./data/langDetection.csv')
    inp = raw.Text.values
    lbl = raw.Language.values
    instance = Train(inp, lbl)
    processed_text = instance.preprocess()
    transformed_labels, classes = instance.label_encode()
    vectorized = instance.vectorize(processed_text)
    model = instance.build(vectorized, transformed_labels)


    model, preds, acc = instance.pipeline_predict(processed_text, transformed_labels)
    model_file: str = "langDetTrained1.joblib"
    model_target_tuple = (model, classes)
    joblib.dump(model_target_tuple, model_file)
    print("Model saved")


if __name__ == '__main__':
    main()