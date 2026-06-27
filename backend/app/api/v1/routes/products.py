from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductRead
from app.services.product_service import (
    list_products,
    get_product,
    create_new_product,
    update_existing_product,
    remove_product
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[ProductRead])
def get_products(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    return list_products(db, skip=skip, limit=limit)


@router.get("/{product_id}", response_model=ProductRead)
def get_single_product(product_id: int, db: Session = Depends(get_db)):
    return get_product(db, product_id)


@router.post("/", response_model=ProductRead)
def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    return create_new_product(db, product_in)


@router.put("/{product_id}", response_model=ProductRead)
def update_product(product_id: int, product_in: ProductUpdate, db: Session = Depends(get_db)):
    return update_existing_product(db, product_id, product_in)


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    remove_product(db, product_id)
    return {"message": "محصول حذف شد"}
