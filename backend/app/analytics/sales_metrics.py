from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.repositories.dashboard_repo import (
    get_sales_sum,
    get_profit_sum,
    get_invoice_count,
    get_active_customers,
    get_new_customers
)


def get_sales_summary(db: Session):
    """خلاصه‌ی فروش/سود برای سرویس‌های AI."""
    return calculate_dashboard_metrics(db)


def calculate_dashboard_metrics(db: Session):
    """محاسبات فروش/سود/مشتری‌ها برای داشبورد."""

    today = datetime.today().date()
    week_start = today - timedelta(days=7)
    month_start = today.replace(day=1)
    year_start = today.replace(month=1, day=1)

    sales_today = get_sales_sum(db, today, today)
    sales_week = get_sales_sum(db, week_start, today)
    sales_month = get_sales_sum(db, month_start, today)
    sales_year = get_sales_sum(db, year_start, today)

    profit_today = get_profit_sum(db, today, today)
    profit_month = get_profit_sum(db, month_start, today)

    invoice_count = get_invoice_count(db, month_start, today)
    active_customers = get_active_customers(db, month_start, today)
    new_customers = get_new_customers(db, month_start, today)

    avg_invoice = sales_month / invoice_count if invoice_count > 0 else 0

    # رشد فروش و سود (ماهانه)
    last_month_start = (month_start - timedelta(days=1)).replace(day=1)
    last_month_end = month_start - timedelta(days=1)

    last_month_sales = get_sales_sum(db, last_month_start, last_month_end)
    last_month_profit = get_profit_sum(db, last_month_start, last_month_end)

    sales_growth = ((sales_month - last_month_sales) / last_month_sales * 100) if last_month_sales > 0 else 0
    profit_growth = ((profit_month - last_month_profit) / last_month_profit * 100) if last_month_profit > 0 else 0

    # تارگت (فعلاً ثابت، بعداً از جدول Targets می‌گیریم)
    target_month = 300_000_000
    target_achievement = (sales_month / target_month * 100)

    return {
        "sales_today": sales_today,
        "sales_week": sales_week,
        "sales_month": sales_month,
        "sales_year": sales_year,
        "profit_today": profit_today,
        "profit_month": profit_month,
        "active_customers": active_customers,
        "new_customers": new_customers,
        "invoice_count": invoice_count,
        "avg_invoice_amount": avg_invoice,
        "sales_growth_percent": sales_growth,
        "profit_growth_percent": profit_growth,
        "sales_target_achievement_percent": target_achievement
    }
