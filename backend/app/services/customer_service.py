from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.customer_repo import (
    list_customers,
    get_customer_by_id,
    create_customer,
    update_customer,
    delete_customer
)
from app.schemas.customer import CustomerCreate, CustomerUpdate


def get_customers(db: Session, skip=0, limit=50):
    return list_customers(db, skip, limit)


def get_single_customer(db: Session, customer_id: int):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="مشتری یافت نشد")
    return customer


def create_new_customer(db: Session, customer_in: CustomerCreate):
    return create_customer(db, customer_in)


def update_existing_customer(db: Session, customer_id: int, customer_in: CustomerUpdate):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="مشتری یافت نشد")
    return update_customer(db, customer, customer_in)


def remove_customer(db: Session, customer_id: int):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="مشتری یافت نشد")
    delete_customer(db, customer)
    return True
