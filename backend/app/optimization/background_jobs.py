import threading
from app.forecasting.forecast_service import generate_forecast
from app.alerts.alert_service import generate_daily_alerts


def run_daily_jobs(db):
    def job():
        generate_forecast(db, model="prophet", days=30)
        generate_daily_alerts(db)

    t = threading.Thread(target=job)
    t.start()
