from app.analytics.sales_metrics import get_sales_summary
from app.analytics.profit_metrics import get_profit_summary


def get_kpis(db):
    sales = get_sales_summary(db)
    profit = get_profit_summary(db)

    return {
        "sales_today": sales["sales_today"],
        "sales_month": sales["sales_month"],
        "profit_today": profit["profit_today"],
        "profit_month": profit["profit_month"]
    }
