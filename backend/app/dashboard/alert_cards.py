from app.alerts.alert_service import generate_daily_alerts


def get_alert_card(db):
    alerts = generate_daily_alerts(db)
    return {
        "title": "هشدارهای امروز",
        "alerts": alerts["alerts"]
    }
