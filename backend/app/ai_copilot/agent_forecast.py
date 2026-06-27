from app.forecasting.forecast_service import generate_forecast


def forecast_agent(db, message: str):
    result = generate_forecast(db, model="prophet", days=30)
    return {
        "type": "forecast",
        "forecast": result
    }
