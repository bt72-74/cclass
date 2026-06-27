from sqlalchemy.orm import Session
from app.forecasting.feature_engineering import load_sales_dataframe
from app.forecasting.prophet_model import forecast_with_prophet
from app.forecasting.xgboost_model import forecast_with_xgboost
from app.forecasting.lstm_model import forecast_with_lstm


def generate_forecast(db: Session, model: str = "prophet", days: int = 30):
    df = load_sales_dataframe(db)

    if df.empty:
        return {"error": "No sales data available"}

    if model == "prophet":
        return forecast_with_prophet(df, days).to_dict(orient="records")

    if model == "xgboost":
        return forecast_with_xgboost(df, days).to_dict(orient="records")

    if model == "lstm":
        return forecast_with_lstm(df, days).to_dict(orient="records")

    return {"error": "Invalid model name"}
