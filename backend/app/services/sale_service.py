from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.sale_repo import (
    create_sale,
    get_sale_by_id,
    list_sales,
    delete_sale
)
from app.schemas.sale import SaleCreate


def create_new_sale(db: Session, sale_in: SaleCreate):
    if not sale_in.items or len(sale_in.items) == 0:
        raise HTTPException(status_code=400, detail="حداقل یک آیتم فروش لازم است.")
    return create_sale(db, sale_in)


def get_single_sale(db: Session, sale_id: int):
    sale = get_sale_by_id(db, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="فاکتور یافت نشد.")
    return sale


def get_sales_list(db: Session, skip=0, limit=50):
    return list_sales(db, skip, limit)


def remove_sale(db: Session, sale_id: int):
    sale = get_sale_by_id(db, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="فاکتور یافت نشد.")
    delete_sale(db, sale)
    return True
