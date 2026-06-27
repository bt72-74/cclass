import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split


def forecast_with_xgboost(df: pd.DataFrame, periods: int = 30):
    df = df.copy()
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year

    X = df[["day", "month", "year"]]
    y = df["sales"]

    model = XGBRegressor()
    model.fit(X, y)

    future_dates = pd.date_range(df["date"].max(), periods=periods + 1)[1:]
    future_df = pd.DataFrame({
        "date": future_dates,
        "day": future_dates.day,
        "month": future_dates.month,
        "year": future_dates.year
    })

    future_df["forecast"] = model.predict(future_df[["day", "month", "year"]])
    return future_df[["date", "forecast"]]
