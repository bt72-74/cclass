from app.forecasting.forecast_service import generate_forecast


def get_forecast_card(db):
    forecast = generate_forecast(db, model="prophet", days=7)
    return {
        "title": "پیش‌بینی فروش ۷ روز آینده",
        "data": forecast
    }
