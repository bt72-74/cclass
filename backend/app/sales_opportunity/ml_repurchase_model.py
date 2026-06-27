import numpy as np
from sklearn.linear_model import LogisticRegression


def train_repurchase_model(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    return model


def predict_repurchase(model, features):
    return model.predict_proba([features])[0][1] * 100
