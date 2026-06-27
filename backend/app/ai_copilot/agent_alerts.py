from app.alerts.alert_service import generate_daily_alerts


def alerts_agent(db, message: str, customer_id: int | None = None):
    return generate_daily_alerts(db, customer_id)
