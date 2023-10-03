#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import joblib
from typing import List
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split as split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

from nltk.corpus import stopwords


stoppies = stopwords.words('english')


class Model(object):
    def __init__(self, inputs, targets) -> None:
        self._x = inputs
        self._y = targets
        self._model = MultinomialNB()

    def fit(self) -> None:
        self._model.fit(self._x, self._y)

    def predict(self, inputs: np.ndarray) -> np.ndarray:
        """ Here input must be a word embedding i.e vectorized text """
        predictions = self._model.predict(inputs)
        return predictions

    def accuracy(self, trues: List[int], preds: List[int]) -> None:
        res = accuracy_score(trues, preds)
        print(f"Accuracy: {res:.2f}")
        return

    def save_model(self, filename: str):
        model_target_tuple = (self._model, self._y)
        joblib.dump(model_target_tuple, filename)
        print("Done...")


def main() -> None:
    raw = pd.read_csv("fraud_email_.csv")
    raw.dropna(inplace=True)

    raw['clean'] = (
        raw['Text'].apply(lambda x: ' '.join(x.lower() for x in x.split()))
        .str.replace(r'[^\w\s]', '', regex=True)
        .apply(lambda x: ' '.join(x for x in x.split() if x not in set(stoppies)))
    )
    vectorizer = TfidfVectorizer(norm='l2', decode_error='ignore', binary=True)
    features = vectorizer.fit_transform(raw.clean.values)

    train_inputs, test_inputs, train_target, test_target = split(
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        features, raw.Class.values, test_size=.30, stratify=raw.Class.values, random_state=42)
||||||| Stash base
        features,
        raw.Class.values,
        test_size=.30,
        stratify=raw.Class.values,
        random_state=42)
=======
        features, raw.Class.values, test_size=.30, stratify=raw.Class.values,random_state=42)
>>>>>>> Stashed changes
||||||| Stash base
        features,
        raw.Class.values,
        test_size=.30,
        stratify=raw.Class.values,
        random_state=42)
=======
        features, raw.Class.values, test_size=.30, stratify=raw.Class.values,random_state=42)
>>>>>>> Stashed changes
||||||| Stash base
        features,
        raw.Class.values,
        test_size=.30,
        stratify=raw.Class.values,
        random_state=42)
=======
        features, raw.Class.values, test_size=.30, stratify=raw.Class.values,random_state=42)
>>>>>>> Stashed changes
||||||| Stash base
        features,
        raw.Class.values,
        test_size=.30,
        stratify=raw.Class.values,
        random_state=42)
=======
        features, raw.Class.values, test_size=.30, stratify=raw.Class.values,random_state=42)
>>>>>>> Stashed changes

    model = Model(train_inputs, train_target)
    model.fit()

<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    filename = "email_phishing_detection.0.1.0.joblib"
    # model.save_model(filename=filename)

||||||| Stash base
    ex = [
        """swapnil.narwade3@gmail.com Job For You <vacancy@job.shine.com> 
        Do Not forward this mail, it contains links which allow direct login to your Shine account. 
        Emailer Dear Swapnil, Recruiter from Mercedes Benz Research And Development India Pvt.Ltd. 
        is actively hiring"""
    ]

    ex_feat = vectorizer.transform(ex)
||||||| Stash base
    ex = [
        """swapnil.narwade3@gmail.com Job For You <vacancy@job.shine.com> 
        Do Not forward this mail, it contains links which allow direct login to your Shine account. 
        Emailer Dear Swapnil, Recruiter from Mercedes Benz Research And Development India Pvt.Ltd. 
        is actively hiring"""
    ]

    ex_feat = vectorizer.transform(ex)
=======
>>>>>>> Stashed changes
||||||| Stash base
    ex = [
        """swapnil.narwade3@gmail.com Job For You <vacancy@job.shine.com> 
        Do Not forward this mail, it contains links which allow direct login to your Shine account. 
        Emailer Dear Swapnil, Recruiter from Mercedes Benz Research And Development India Pvt.Ltd. 
        is actively hiring"""
    ]

    ex_feat = vectorizer.transform(ex)
=======
>>>>>>> Stashed changes
||||||| Stash base
    ex = [
        """swapnil.narwade3@gmail.com Job For You <vacancy@job.shine.com> 
        Do Not forward this mail, it contains links which allow direct login to your Shine account. 
        Emailer Dear Swapnil, Recruiter from Mercedes Benz Research And Development India Pvt.Ltd. 
        is actively hiring"""
    ]

    ex_feat = vectorizer.transform(ex)
=======
>>>>>>> Stashed changes
    filename = "phishing.joblib"
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    model.save_model(filename=filename)

=======
    filename = "phishing.joblib"
    model.save_model(filename=filename)
||||||| Stash base
    # model.save_model(filename=filename)

    m2, _ = joblib.load(filename=filename)
    ex_pred = m2.predict(ex_feat)
    print(ex_pred)
=======
    model.save_model(filename=filename)
>>>>>>> Stashed changes
||||||| Stash base
    # model.save_model(filename=filename)

    m2, _ = joblib.load(filename=filename)
    ex_pred = m2.predict(ex_feat)
    print(ex_pred)
=======
    model.save_model(filename=filename)
>>>>>>> Stashed changes

>>>>>>> Stashed changes

if __name__ == "__main__":
    main()
