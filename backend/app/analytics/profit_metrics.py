from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.models.sale import Sale


def get_profit_summary(db: Session):
    today = datetime.utcnow().date()
    month_start = today.replace(day=1)

    profit_today = db.query(func.sum(Sale.total_profit))\
        .filter(func.date(Sale.invoice_date) == today).scalar() or 0

    profit_month = db.query(func.sum(Sale.total_profit))\
        .filter(Sale.invoice_date >= month_start).scalar() or 0

    return {
        "profit_today": profit_today,
        "profit_month": profit_month
    }


def get_top_profit_products(db: Session, limit: int = 10):
    from app.models.sale_item import SaleItem

    rows = db.query(
        SaleItem.product_id,
        func.sum(SaleItem.line_profit).label("profit")
    ).group_by(
        SaleItem.product_id
    ).order_by(
        func.sum(SaleItem.line_profit).desc()
    ).limit(limit).all()

    return [{"product_id": r.product_id, "profit": r.profit} for r in rows]
