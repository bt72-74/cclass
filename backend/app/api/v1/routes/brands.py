from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.brand import BrandCreate, BrandUpdate, BrandRead
from app.services.brand_service import (
    get_brands,
    get_single_brand,
    create_new_brand,
    update_existing_brand,
    remove_brand,
)

router = APIRouter(prefix="/brands", tags=["Brands"])


@router.get("/", response_model=list[BrandRead])
def list_brands_endpoint(db: Session = Depends(get_db)):
    return get_brands(db)


@router.get("/{brand_id}", response_model=BrandRead)
def get_brand_endpoint(brand_id: int, db: Session = Depends(get_db)):
    return get_single_brand(db, brand_id)


@router.post("/", response_model=BrandRead)
def create_brand_endpoint(brand_in: BrandCreate, db: Session = Depends(get_db)):
    return create_new_brand(db, brand_in)


@router.put("/{brand_id}", response_model=BrandRead)
def update_brand_endpoint(brand_id: int, brand_in: BrandUpdate, db: Session = Depends(get_db)):
    return update_existing_brand(db, brand_id, brand_in)


@router.delete("/{brand_id}")
def delete_brand_endpoint(brand_id: int, db: Session = Depends(get_db)):
    remove_brand(db, brand_id)
    return {"message": "برند حذف شد"}
