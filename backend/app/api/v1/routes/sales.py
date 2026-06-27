from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.sale import SaleCreate, SaleRead
from app.services.sale_service import (
    create_new_sale,
    get_single_sale,
    get_sales_list,
    remove_sale
)

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.get("/", response_model=list[SaleRead])
def list_sales_endpoint(db: Session = Depends(get_db)):
    return get_sales_list(db)


@router.get("/{sale_id}", response_model=SaleRead)
def get_sale_endpoint(sale_id: int, db: Session = Depends(get_db)):
    return get_single_sale(db, sale_id)


@router.post("/", response_model=SaleRead)
def create_sale_endpoint(sale_in: SaleCreate, db: Session = Depends(get_db)):
    return create_new_sale(db, sale_in)


@router.delete("/{sale_id}")
def delete_sale_endpoint(sale_id: int, db: Session = Depends(get_db)):
    remove_sale(db, sale_id)
    return {"message": "فاکتور حذف شد"}
