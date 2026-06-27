from sqlalchemy.orm import Session
from app.models.brand import Brand
from app.schemas.brand import BrandCreate, BrandUpdate


def list_brands(db: Session):
    return db.query(Brand).all()


def get_brand_by_id(db: Session, brand_id: int):
    return db.query(Brand).filter(Brand.id == brand_id).first()


def create_brand(db: Session, brand_in: BrandCreate):
    brand = Brand(**brand_in.dict())
    db.add(brand)
    db.commit()
    db.refresh(brand)
    return brand


def update_brand(db: Session, brand: Brand, brand_in: BrandUpdate):
    for field, value in brand_in.dict().items():
        setattr(brand, field, value)
    db.commit()
    db.refresh(brand)
    return brand


def delete_brand(db: Session, brand: Brand):
    db.delete(brand)
    db.commit()
