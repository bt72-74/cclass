from sqlalchemy.orm import Session
from app.analytics.sales_metrics import get_sales_summary
from app.analytics.profit_metrics import get_profit_summary
from app.analytics.customer_metrics import get_customer_lifetime_value
from app.forecasting.forecast_service import generate_forecast
from app.alerts.alert_service import generate_daily_alerts


def execute_query(db: Session, query: dict):
    qtype = query["type"]

    if qtype == "sales_summary":
        return get_sales_summary(db)

    if qtype == "profit_summary":
        return get_profit_summary(db)

    if qtype == "customer_info":
        cid = query.get("customer_id")
        return {
            "customer_id": cid,
            "lifetime_value": get_customer_lifetime_value(db, cid)
        }

    if qtype == "forecast":
        return generate_forecast(db, model=query.get("model"))

    if qtype == "alerts":
        return generate_daily_alerts(db, customer_id=query.get("customer_id"))

    return {"error": "Unknown query type"}
