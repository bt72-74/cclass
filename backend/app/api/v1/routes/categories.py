from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryRead
from app.services.category_service import (
    get_categories,
    get_single_category,
    create_new_category,
    update_existing_category,
    remove_category,
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryRead])
def list_categories_endpoint(db: Session = Depends(get_db)):
    return get_categories(db)


@router.get("/{category_id}", response_model=CategoryRead)
def get_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    return get_single_category(db, category_id)


@router.post("/", response_model=CategoryRead)
def create_category_endpoint(category_in: CategoryCreate, db: Session = Depends(get_db)):
    return create_new_category(db, category_in)


@router.put("/{category_id}", response_model=CategoryRead)
def update_category_endpoint(category_id: int, category_in: CategoryUpdate, db: Session = Depends(get_db)):
    return update_existing_category(db, category_id, category_in)


@router.delete("/{category_id}")
def delete_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    remove_category(db, category_id)
    return {"message": "دسته‌بندی حذف شد"}
