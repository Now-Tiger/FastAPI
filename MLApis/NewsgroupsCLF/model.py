#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import joblib

import pandas as pd
import numpy as np

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (accuracy_score, confusion_matrix)
from sklearn.model_selection import train_test_split as split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


categories = [
    "soc.religion.christian",
    "talk.religion.misc",
    "comp.sys.mac.hardware",
    "sci.crypt",
]

newsgroups_training = fetch_20newsgroups(subset="train", categories=categories, random_state=42,)
newsgroups_testing = fetch_20newsgroups(subset="test", categories=categories, random_state=42,)

print(newsgroups_training.data[0])
print(np.unique(newsgroups_training.target))    # 0 1 2 3

model = make_pipeline(TfidfVectorizer(), MultinomialNB(),)
model.fit(newsgroups_training.data, newsgroups_training.target)

# Run predictions on testing data
predictions = model.predict(newsgroups_testing.data)

# compute accuracy
accuracy = accuracy_score(newsgroups_testing.target, predictions)
print(f"Accuracy: {accuracy:.3f}")


# confusion matrix
confusion_mat = confusion_matrix(newsgroups_testing.target, predictions)
confusion_df = pd.DataFrame(
    confusion_mat,
    index=pd.Index(newsgroups_testing.target_names, name="True"),
    columns=pd.Index(newsgroups_testing.target_names, name="Predicted"),
)

print(confusion_df)

model_file: str = "newsgroups_model.joblib"
model_target_tuple = (model, newsgroups_training.target_names)
joblib.dump(model_target_tuple, model_file)