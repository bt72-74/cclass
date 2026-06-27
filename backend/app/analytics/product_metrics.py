from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.sale_item import SaleItem
from app.models.product import Product


def get_slow_moving_products(db: Session, limit: int = 10):
    rows = db.query(
        Product.id,
        Product.name,
        func.sum(SaleItem.quantity).label("qty")
    ).join(
        Product, Product.id == SaleItem.product_id
    ).group_by(
        Product.id
    ).order_by(
        func.sum(SaleItem.quantity).asc()
    ).limit(limit).all()

    return [{"id": r.id, "name": r.name, "quantity": r.qty} for r in rows]


def get_high_margin_products(db: Session, limit: int = 10):
    rows = db.query(
        Product.id,
        Product.name,
        Product.margin_percent
    ).order_by(
        Product.margin_percent.desc()
    ).limit(limit).all()

    return [{"id": r.id, "name": r.name, "margin": r.margin_percent} for r in rows]
