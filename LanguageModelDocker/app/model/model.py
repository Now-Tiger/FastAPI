#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import string
import pickle
from pathlib import Path


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


def predict_pipeline(txt: str) -> str:
    txt = re.sub(r'[!@#$(),\n"%^*?\:;`0-9]', ' ', txt)
    txt = re.sub('https?://\S+|www\.\S+', '', txt)
    txt = re.sub('[%s]' % re.escape(string.punctuation), '', txt)
    txt = re.sub(r"^\s+|\s+$", "", txt)
    txt = re.sub(r'[^\w\s]', '', txt)
    txt = re.sub('<.*?>+', '', txt)
    txt = re.sub(' +', ' ', txt)
    txt = re.sub(r'[[]]', ' ', txt)
    txt = txt.lower()
    pred = model.predict([txt])
    return classes[pred[0]]