from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.models.sale import Sale
from app.models.customer import Customer
from app.models.sale_item import SaleItem
from app.models.product import Product
from app.models.salesperson import SalesPerson


def get_sales_sum(db: Session, start_date, end_date):
    return db.query(func.sum(Sale.total_amount))\
        .filter(Sale.invoice_date >= start_date)\
        .filter(Sale.invoice_date <= end_date)\
        .scalar() or 0


def get_profit_sum(db: Session, start_date, end_date):
    return db.query(func.sum(Sale.total_profit))\
        .filter(Sale.invoice_date >= start_date)\
        .filter(Sale.invoice_date <= end_date)\
        .scalar() or 0


def get_invoice_count(db: Session, start_date, end_date):
    return db.query(func.count(Sale.id))\
        .filter(Sale.invoice_date >= start_date)\
        .filter(Sale.invoice_date <= end_date)\
        .scalar() or 0


def get_active_customers(db: Session, start_date, end_date):
    return db.query(func.count(func.distinct(Sale.customer_id)))\
        .filter(Sale.invoice_date >= start_date)\
        .filter(Sale.invoice_date <= end_date)\
        .scalar() or 0


def get_new_customers(db: Session, start_date, end_date):
    return db.query(Customer)\
        .filter(Customer.created_at >= start_date)\
        .filter(Customer.created_at <= end_date)\
        .count()
