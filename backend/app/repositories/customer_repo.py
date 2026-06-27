from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate


def list_customers(db: Session, skip: int = 0, limit: int = 50):
    return db.query(Customer).offset(skip).limit(limit).all()


def get_customer_by_id(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()


def create_customer(db: Session, customer_in: CustomerCreate):
    customer = Customer(**customer_in.dict())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def update_customer(db: Session, customer: Customer, customer_in: CustomerUpdate):
    for field, value in customer_in.dict(exclude_unset=True).items():
        setattr(customer, field, value)
    db.commit()
    db.refresh(customer)
    return customer


def delete_customer(db: Session, customer: Customer):
    db.delete(customer)
    db.commit()

