from sqlalchemy.orm import Session
from app.analytics.sales_metrics import calculate_dashboard_metrics
from app.schemas.dashboard import DashboardSummary, ChartData


def get_dashboard_summary(db: Session) -> DashboardSummary:
    metrics = calculate_dashboard_metrics(db)

    # نمودارهای نمونه (بعداً واقعی می‌کنیم)
    daily_sales = ChartData(labels=["شنبه", "یکشنبه", "دوشنبه"], values=[12, 18, 25])
    weekly_sales = ChartData(labels=["هفته 1", "هفته 2"], values=[120, 150])
    monthly_sales = ChartData(labels=["فروردین", "اردیبهشت"], values=[300, 350])
    category_share = ChartData(labels=["دفتر", "خودکار"], values=[40, 60])
    salesperson_share = ChartData(labels=["علی", "رضا"], values=[55, 45])

    return DashboardSummary(
        **metrics,
        daily_sales_trend=daily_sales,
        weekly_sales_trend=weekly_sales,
        monthly_sales_trend=monthly_sales,
        category_share=category_share,
        salesperson_share=salesperson_share
    )
