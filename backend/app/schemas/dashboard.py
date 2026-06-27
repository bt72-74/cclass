from pydantic import BaseModel
from typing import List, Any


class ChartData(BaseModel):
    labels: List[str]
    values: List[float]


class DashboardSummary(BaseModel):
    sales_today: float
    sales_week: float
    sales_month: float
    sales_year: float

    profit_today: float
    profit_month: float

    active_customers: int
    new_customers: int
    invoice_count: int
    avg_invoice_amount: float

    sales_growth_percent: float
    profit_growth_percent: float
    sales_target_achievement_percent: float

    daily_sales_trend: ChartData
    weekly_sales_trend: ChartData
    monthly_sales_trend: ChartData
    category_share: ChartData
    salesperson_share: ChartData
