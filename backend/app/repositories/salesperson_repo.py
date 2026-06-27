from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
from app.models.salesperson import SalesPerson
from app.models.sale import Sale
from app.schemas.salesperson import SalesPersonCreate, SalesPersonUpdate


def list_salespersons(db: Session, skip=0, limit=50):
    return db.query(SalesPerson).offset(skip).limit(limit).all()


def get_salesperson_by_id(db: Session, sp_id: int):
    return db.query(SalesPerson).filter(SalesPerson.id == sp_id).first()


def create_salesperson(db: Session, sp_in: SalesPersonCreate):
    sp = SalesPerson(**sp_in.dict())
    db.add(sp)
    db.commit()
    db.refresh(sp)
    return sp


def update_salesperson(db: Session, sp: SalesPerson, sp_in: SalesPersonUpdate):
    for field, value in sp_in.dict().items():
        setattr(sp, field, value)
    db.commit()
    db.refresh(sp)
    return sp


def delete_salesperson(db: Session, sp: SalesPerson):
    db.delete(sp)
    db.commit()


def get_salespersons_performance(db: Session, start_date=None, end_date=None):
    """
    برای هر فروشنده: مجموع فروش، مجموع سود، تعداد فاکتور و درصد سوددهی
    """
    query = db.query(
        SalesPerson.id,
        SalesPerson.code,
        SalesPerson.name,
        SalesPerson.phone,
        SalesPerson.email,
        SalesPerson.is_active,
        func.coalesce(func.sum(Sale.total_amount), 0).label("total_sales"),
        func.coalesce(func.sum(Sale.total_profit), 0).label("total_profit"),
        func.coalesce(func.count(Sale.id), 0).label("invoice_count"),
    ).outerjoin(
        Sale,
        (Sale.salesperson_id == SalesPerson.id) & (Sale.status == "Paid")
    )

    if start_date:
        query = query.filter(Sale.invoice_date >= start_date)
    if end_date:
        query = query.filter(Sale.invoice_date <= end_date)

    rows = query.group_by(
        SalesPerson.id,
        SalesPerson.code,
        SalesPerson.name,
        SalesPerson.phone,
        SalesPerson.email,
        SalesPerson.is_active,
    ).order_by(
        func.coalesce(func.sum(Sale.total_amount), 0).desc()
    ).all()

    result = []
    for r in rows:
        profit_margin = (r.total_profit / r.total_sales * 100) if r.total_sales > 0 else 0
        result.append({
            "id": r.id,
            "code": r.code,
            "name": r.name,
            "phone": r.phone,
            "email": r.email,
            "is_active": r.is_active,
            "total_sales": round(r.total_sales, 2),
            "total_profit": round(r.total_profit, 2),
            "invoice_count": r.invoice_count,
            "profit_margin_percent": round(profit_margin, 2),
        })

    return result
