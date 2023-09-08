#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split as split
from sklearn.preprocessing import StandardScaler


def normalize(data: np.ndarray) -> np.ndarray:
    num_cols = [col for col in data.columns if data[col].dtype in ['float']]
    scaler = StandardScaler().fit(data[num_cols])
    data[num_cols] = scaler.transform(data[num_cols])
    return data[num_cols]


def main() -> None:
    raw, target = load_iris(as_frame=True, return_X_y=True)
    raw = normalize(raw)
    train_inp, test_inp, train_target, test_targt = split(
        raw, target, test_size=.25, random_state=42)

    model = LogisticRegression(
        max_iter=300,
        solver='liblinear',
        random_state=42
    ).fit(train_inp, train_target)
    
    train_preds = model.predict(train_inp)
    train_acc = accuracy_score(train_target, train_preds)
    print(f"Train accuracy: {train_acc:.3f}")
    return


if __name__ == '__main__':
    main()
