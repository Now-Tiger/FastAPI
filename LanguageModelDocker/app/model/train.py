#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import string
import pickle

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split as split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, f1_score

from warnings import filterwarnings
filterwarnings('ignore')


class Train(object):
    def __init__(self, x: np.ndarray, Y: np.ndarray) -> None:
        self._inputs = x
        self._labels = Y

    def peek(self) -> np.ndarray:
        return self._inputs[:5]

    def label_encode(self) -> tuple[np.ndarray, np.ndarray]:
        encoder = LabelEncoder().fit(self._labels)
        transformed = encoder.transform(self._labels)
        return transformed, encoder.classes_

    def preprocess(self) -> list:
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

    def tokenizer(self, txt: list[str]) -> None:
        # Implement tokenizer wither stemming and pass it to the countvectorizer.
        pass

<<<<<<< HEAD
    def model(self, inputs: np.ndarray, target: np.ndarray) -> tuple[object, np.float64]:
        clf = LogisticRegression(
            max_iter=300, C=0.1,random_state=42, solver='sag').fit(inputs, target)
||||||| 62a7687
    def model(self, inputs: np.ndarray, target: np.ndarray) -> tuple[any, np.float64]:
        clf = LogisticRegression(
            max_iter=300,
            C=0.1,
            random_state=42,
            solver='sag'
        ).fit(inputs, target)
=======
    def model(self, inputs: np.ndarray, target: np.ndarray) -> tuple[any, np.float64]:
        clf = MultinomialNB().fit(inputs, target)
>>>>>>> 6533be920b96cbb32e03efbe0acc0a9569f33825
        preds = clf.predict(inputs)
        return (clf, preds)

    def build(self, inputs: list[str], train_targets: np.ndarray) -> None:
        """ FIXES: PLEASE CLEAN UP THIS HORRIBLE MESSSSSS 
            ?NEW: FIX ABOVE METHODE.. FUNCTION NOT ABLE TO SAVE MODEL INTO PICKLE
        """
        train_transformed = self.vectorize(inputs).toarray()
        clf, preds = self.model(train_transformed, train_targets)
        _, f1 = self.accuracy(train_targets, preds)

        if f1 >= 0.88:
            print("Saving model as a pickle fiile...")
            self.dump(clf)
        else:
            print("Modify the model...")

    def accuracy(self, targets: np.ndarray, preds: np.ndarray) -> tuple[np.float64, np.float64]:
        acc = accuracy_score(targets, preds)
        f1 = f1_score(targets, preds, average='weighted')
        return (acc, f1)

    def vectorize(self, inputs: list[str]) -> np.ndarray:
        cv = CountVectorizer(max_features=1000, lowercase=True)
        cv.fit(inputs)
        transformed = cv.transform(inputs).toarray()
        return transformed

    def dump(self, model: any) -> None:
        with open("train_model_pipeline-0.1.0.pkl", "wb") as file:
            pickle.dump(model, file)
        return


def main() -> None:
    raw = pd.read_csv('./data/langDetection.csv')
    inp = raw.Text.values
    lbl = raw.Language.values
    instance = Train(inp, lbl)
    labels, classes = instance.label_encode()
    processed_texts = instance.preprocess()
    train_inp, test_inp, train_target, test_target = split(
        processed_texts, labels, test_size=0.30, random_state=42, stratify=labels, shuffle=True
    )
    # print(train_inp[:9])
<<<<<<< HEAD
    instance.build(train_inp, train_target)
    with open("train_model_pipeline-0.1.0.pkl", "rb") as file:
        model = pickle.load(file=file)
    
    pred = model.predict(["Hello there"])
    print(pred)
||||||| 62a7687
    # instance.build(train_inp, train_target)
=======
    instance.build(train_inp, train_target)
>>>>>>> 6533be920b96cbb32e03efbe0acc0a9569f33825


if __name__ == '__main__':
    main()
