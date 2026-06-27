from sqlalchemy.orm import Session
from app.analytics.sales_metrics import get_sales_summary
from app.analytics.profit_metrics import get_profit_summary
from app.analytics.customer_metrics import get_churn_risk
from app.alerts.evaluator import evaluate_alerts


def generate_daily_alerts(db: Session, customer_id: int | None = None):
    data = {}

    # فروش
    sales_summary = get_sales_summary(db)
    data["sales_today"] = sales_summary["sales_today"]

    # سود
    profit_summary = get_profit_summary(db)
    data["profit_today"] = profit_summary["profit_today"]

    # ریزش مشتری (اگر مشتری مشخص شده باشد)
    if customer_id:
        data["churn_risk"] = get_churn_risk(db, customer_id)

    # ارزیابی قوانین
    alerts = evaluate_alerts(data)

    return {
        "data": data,
        "alerts": alerts
    }
