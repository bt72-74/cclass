from app.analytics.sales_metrics import get_sales_summary


def sales_agent(db, message: str):
    summary = get_sales_summary(db)
    return {
        "type": "sales",
        "analysis": f"فروش امروز {summary['sales_today']} و فروش ماه {summary['sales_month']} است.",
        "data": summary
    }
