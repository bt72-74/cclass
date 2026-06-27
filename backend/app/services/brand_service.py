from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.brand_repo import (
    list_brands,
    get_brand_by_id,
    create_brand,
    update_brand,
    delete_brand,
)
from app.schemas.brand import BrandCreate, BrandUpdate


def get_brands(db: Session):
    return list_brands(db)


def get_single_brand(db: Session, brand_id: int):
    brand = get_brand_by_id(db, brand_id)
    if not brand:
        raise HTTPException(status_code=404, detail="برند یافت نشد")
    return brand


def create_new_brand(db: Session, brand_in: BrandCreate):
    return create_brand(db, brand_in)


def update_existing_brand(db: Session, brand_id: int, brand_in: BrandUpdate):
    brand = get_brand_by_id(db, brand_id)
    if not brand:
        raise HTTPException(status_code=404, detail="برند یافت نشد")
    return update_brand(db, brand, brand_in)


def remove_brand(db: Session, brand_id: int):
    brand = get_brand_by_id(db, brand_id)
    if not brand:
        raise HTTPException(status_code=404, detail="برند یافت نشد")
    delete_brand(db, brand)
    return True
