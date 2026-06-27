from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.product_repo import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product
)
from app.schemas.product import ProductCreate, ProductUpdate


def list_products(db: Session, skip=0, limit=1000):
    return get_all_products(db, skip, limit)


def get_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="محصول یافت نشد")
    return product


def create_new_product(db: Session, product_in: ProductCreate):
    return create_product(db, product_in)


def update_existing_product(db: Session, product_id: int, product_in: ProductUpdate):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="محصول یافت نشد")
    return update_product(db, product, product_in)


def remove_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="محصول یافت نشد")
    delete_product(db, product)
    return True
