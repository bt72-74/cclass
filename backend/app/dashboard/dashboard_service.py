from app.dashboard.kpi_engine import get_kpis
from app.dashboard.insights_engine import generate_insights
from app.dashboard.forecast_cards import get_forecast_card
from app.dashboard.alert_cards import get_alert_card


def get_dashboard(db):
    kpis = get_kpis(db)
    insights = generate_insights(kpis)
    forecast = get_forecast_card(db)
    alerts = get_alert_card(db)

    return {
        "kpis": kpis,
        "insights": insights,
        "forecast": forecast,
        "alerts": alerts
    }
