from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime

from app.repositories.salesperson_repo import (
    list_salespersons,
    get_salesperson_by_id,
    create_salesperson,
    update_salesperson,
    delete_salesperson,
    get_salespersons_performance,
)
from app.schemas.salesperson import SalesPersonCreate, SalesPersonUpdate


def get_salespersons(db: Session, skip=0, limit=50):
    return list_salespersons(db, skip, limit)


def get_single_salesperson(db: Session, sp_id: int):
    sp = get_salesperson_by_id(db, sp_id)
    if not sp:
        raise HTTPException(status_code=404, detail="کارشناس فروش یافت نشد")
    return sp


def create_new_salesperson(db: Session, sp_in: SalesPersonCreate):
    return create_salesperson(db, sp_in)


def update_existing_salesperson(db: Session, sp_id: int, sp_in: SalesPersonUpdate):
    sp = get_salesperson_by_id(db, sp_id)
    if not sp:
        raise HTTPException(status_code=404, detail="کارشناس فروش یافت نشد")
    return update_salesperson(db, sp, sp_in)


def remove_salesperson(db: Session, sp_id: int):
    sp = get_salesperson_by_id(db, sp_id)
    if not sp:
        raise HTTPException(status_code=404, detail="کارشناس فروش یافت نشد")
    delete_salesperson(db, sp)
    return True


def get_performance_report(
    db: Session,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
):
    return get_salespersons_performance(db, start_date, end_date)
