#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import string
import joblib

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split as split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import make_pipeline

from warnings import filterwarnings
filterwarnings('ignore')


def preprocess(text: str) -> list:
        # Proper text processing is required stopwords removals, etc.
    table = list()
    for txt in text:
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

def label_encode(targets: np.array) -> tuple[np.ndarray, np.ndarray]:
    encoder = LabelEncoder().fit(targets)
    transformed = encoder.transform(targets)
    return transformed, encoder.classes_

def pipeline_predict(inputs: list, targets: list) -> tuple[np.ndarray, np.float64]:
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(inputs, targets)
    preds = model.predict(inputs)
    accuracy = accuracy_score(preds, targets)
    return (model, preds, accuracy)
 

def summary(targets: np.ndarray, predictions: np.ndarray, classes) -> pd.DataFrame:
    confusion_mat = confusion_matrix(targets, predictions)
    confusion_df = pd.DataFrame(
        confusion_mat,
        index=pd.Index(classes, name="True"),
        columns=pd.Index(classes, name="Predicted"),
    )
    return confusion_df

def main() -> None:
    raw = pd.read_csv('./data/langDetection.csv')
    inp = raw.Text.values
    lbl = raw.Language.values
    processed_text = preprocess(inp)
    transformed_labels, classes = label_encode(lbl)
    model, preds, acc = pipeline_predict(processed_text, transformed_labels)
    model_file: str = "langDetTrained.joblib"
    model_target_tuple = (model, classes)
    joblib.dump(model_target_tuple, model_file)
    print("Model saved")


if __name__ == '__main__':
    main()