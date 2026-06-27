from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.models.sale import Sale
from app.models.sale_item import SaleItem


def get_daily_sales(db: Session, days: int = 30):
    end = datetime.utcnow()
    start = end - timedelta(days=days)

    rows = db.query(
        func.date(Sale.invoice_date).label("day"),
        func.sum(Sale.total_amount).label("sales")
    ).filter(
        Sale.invoice_date >= start
    ).group_by(
        func.date(Sale.invoice_date)
    ).order_by(
        func.date(Sale.invoice_date)
    ).all()

    return [{"day": str(r.day), "sales": r.sales} for r in rows]


def get_top_products(db: Session, limit: int = 10):
    rows = db.query(
        SaleItem.product_id,
        func.sum(SaleItem.quantity).label("qty")
    ).group_by(
        SaleItem.product_id
    ).order_by(
        func.sum(SaleItem.quantity).desc()
    ).limit(limit).all()

    return [{"product_id": r.product_id, "quantity": r.qty} for r in rows]


def get_sales_summary(db: Session):
    today = datetime.utcnow().date()
    month_start = today.replace(day=1)

    sales_today = db.query(func.sum(Sale.total_amount))\
        .filter(func.date(Sale.invoice_date) == today).scalar() or 0

    sales_month = db.query(func.sum(Sale.total_amount))\
        .filter(Sale.invoice_date >= month_start).scalar() or 0

    return {
        "sales_today": sales_today,
        "sales_month": sales_month
    }
