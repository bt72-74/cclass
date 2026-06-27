import numpy as np


def customer_embedding(total_spent, churn_risk, avg_purchase_gap):
    return np.array([
        total_spent / 1_000_000,
        churn_risk / 100,
        avg_purchase_gap / 180
    ])
