from app.alerts.rules import (
    low_sales_rule,
    low_profit_rule,
    churn_risk_rule,
    low_stock_rule
)


def evaluate_alerts(data: dict):
    alerts = []

    if "sales_today" in data and low_sales_rule(data["sales_today"]):
        alerts.append("کاهش فروش امروز")

    if "profit_today" in data and low_profit_rule(data["profit_today"]):
        alerts.append("کاهش سود امروز")

    if "churn_risk" in data and churn_risk_rule(data["churn_risk"]):
        alerts.append("ریسک ریزش مشتری")

    if "stock_qty" in data and low_stock_rule(data["stock_qty"]):
        alerts.append("موجودی کم محصول")

    return alerts
