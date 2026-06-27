from prophet import Prophet
import pandas as pd


def forecast_with_prophet(df: pd.DataFrame, periods: int = 30):
    df_prophet = df.rename(columns={"date": "ds", "sales": "y"})

    model = Prophet()
    model.fit(df_prophet)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
