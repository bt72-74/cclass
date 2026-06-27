from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.customer import CustomerCreate, CustomerUpdate, CustomerRead
from app.services.customer_service import (
    get_customers,
    get_single_customer,
    create_new_customer,
    update_existing_customer,
    remove_customer
)

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/", response_model=list[CustomerRead])
def list_customers_endpoint(db: Session = Depends(get_db)):
    return get_customers(db)


@router.get("/{customer_id}", response_model=CustomerRead)
def get_customer_endpoint(customer_id: int, db: Session = Depends(get_db)):
    return get_single_customer(db, customer_id)


@router.post("/", response_model=CustomerRead)
def create_customer_endpoint(customer_in: CustomerCreate, db: Session = Depends(get_db)):
    return create_new_customer(db, customer_in)


@router.put("/{customer_id}", response_model=CustomerRead)
def update_customer_endpoint(customer_id: int, customer_in: CustomerUpdate, db: Session = Depends(get_db)):
    return update_existing_customer(db, customer_id, customer_in)


@router.delete("/{customer_id}")
def delete_customer_endpoint(customer_id: int, db: Session = Depends(get_db)):
    remove_customer(db, customer_id)
    return {"message": "مشتری حذف شد"}
