from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.core.database import get_db
from app.schemas.salesperson import (
    SalesPersonCreate,
    SalesPersonUpdate,
    SalesPersonRead,
    SalesPersonPerformance,
)
from app.services.salesperson_service import (
    get_salespersons,
    get_single_salesperson,
    create_new_salesperson,
    update_existing_salesperson,
    remove_salesperson,
    get_performance_report,
)

router = APIRouter(prefix="/salespersons", tags=["SalesPersons"])


@router.get("/", response_model=list[SalesPersonRead])
def list_salespersons_endpoint(db: Session = Depends(get_db)):
    return get_salespersons(db)


@router.get("/performance", response_model=List[SalesPersonPerformance])
def salespersons_performance_endpoint(
    start_date: Optional[datetime] = Query(None, description="تاریخ شروع فیلتر"),
    end_date: Optional[datetime] = Query(None, description="تاریخ پایان فیلتر"),
    db: Session = Depends(get_db),
):
    """
    گزارش عملکرد فروشندگان: مجموع فروش، سود، تعداد فاکتور و درصد سوددهی
    """
    return get_performance_report(db, start_date, end_date)


@router.get("/{sp_id}", response_model=SalesPersonRead)
def get_salesperson_endpoint(sp_id: int, db: Session = Depends(get_db)):
    return get_single_salesperson(db, sp_id)


@router.post("/", response_model=SalesPersonRead)
def create_salesperson_endpoint(sp_in: SalesPersonCreate, db: Session = Depends(get_db)):
    return create_new_salesperson(db, sp_in)


@router.put("/{sp_id}", response_model=SalesPersonRead)
def update_salesperson_endpoint(sp_id: int, sp_in: SalesPersonUpdate, db: Session = Depends(get_db)):
    return update_existing_salesperson(db, sp_id, sp_in)


@router.delete("/{sp_id}")
def delete_salesperson_endpoint(sp_id: int, db: Session = Depends(get_db)):
    remove_salesperson(db, sp_id)
    return {"message": "کارشناس فروش حذف شد"}
