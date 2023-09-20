#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import joblib

import pandas as pd
import numpy as np

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split as split
from sklearn.naive_bayes import MultinomialNB


data = pd.read_csv('fraud_email_.csv')
data.dropna(inplace=True)
stoppies = stopwords.words('english')


def process_text(sent: str) -> list[str]:
    """ function to clean redundant string values 
        from array of strings returns a cleaned 
        string values removing unwanted symbols and 
        numbers.
        ----
        text: string values
    """
    for text in sent.split('-'):
        txt = re.sub('[^\w\s]' '', text)
        txt = txt.lower()
    return txt


def tokenizer(text: str) -> list[str]:
    stemmer = SnowballStemmer(language='english')
    return [stemmer.stem(word) for word in word_tokenize(text)]


def vectorize(inputs: list[str]) -> np.ndarray[np.float64]:
    vectorizer = TfidfVectorizer(
        tokenizer=tokenizer,
        stop_words=stoppies,
        decode_error='ignore',
        norm='l2',
        binary=True,)
    transformed = vectorizer.fit_transform(inputs).toarray()
    return transformed


def main() -> None:
    data['clean'] = (
        data.Text.apply(lambda x: ' '.join(x.lower() for x in x.split()))
        .str.replace(r'[^\w\s]', '', regex=True)
        .apply(lambda x: ' '.join(x for x in x.split() if x not in set(stoppies)))
    )

    transformed = vectorize(data.clean.values)

    # split dataset
    train_inputs, val_inputs, train_target, val_target = split(
        transformed, data.Class.values, test_size=.30, random_state=42, stratify=data.Class.values,
    )

    classes = data.Class.values
    base_model = MultinomialNB().fit(train_inputs, train_target)

    model_file = "emailsPhishDetect.0.1.0.joblib"
    model_target_tuple = (base_model, classes)
    joblib.dump(model_target_tuple, model_file)
    return


if __name__ == "__main__":
    main()
