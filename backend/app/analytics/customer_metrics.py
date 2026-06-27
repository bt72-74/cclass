from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.models.sale import Sale


def get_customer_lifetime_value(db: Session, customer_id: int):
    total = db.query(func.sum(Sale.total_amount))\
        .filter(Sale.customer_id == customer_id).scalar() or 0
    return total


def get_customer_last_purchase(db: Session, customer_id: int):
    row = db.query(Sale.invoice_date)\
        .filter(Sale.customer_id == customer_id)\
        .order_by(Sale.invoice_date.desc()).first()

    return row[0] if row else None


def get_churn_risk(db: Session, customer_id: int):
    last_purchase = get_customer_last_purchase(db, customer_id)
    if not last_purchase:
        return 100  # مشتری بدون خرید = ریسک ۱۰۰٪

    days = (datetime.utcnow() - last_purchase).days

    if days > 180:
        return 90
    if days > 90:
        return 70
    if days > 60:
        return 40
    return 10
