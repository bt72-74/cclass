from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def get_all_products(db: Session, skip=0, limit=50):
    return db.query(Product).offset(skip).limit(limit).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, product_in: ProductCreate):
    margin = ((product_in.sale_price - product_in.cost_price) / product_in.sale_price) * 100

    product = Product(
        **product_in.dict(),
        margin_percent=margin
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product: Product, product_in: ProductUpdate):
    margin = ((product_in.sale_price - product_in.cost_price) / product_in.sale_price) * 100

    for field, value in product_in.dict().items():
        setattr(product, field, value)

    product.margin_percent = margin

    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product: Product):
    db.delete(product)
    db.commit()
    