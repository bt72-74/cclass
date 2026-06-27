from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.category_repo import (
    list_categories,
    get_category_by_id,
    create_category,
    update_category,
    delete_category,
)
from app.schemas.category import CategoryCreate, CategoryUpdate


def get_categories(db: Session):
    return list_categories(db)


def get_single_category(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="دسته‌بندی یافت نشد")
    return category


def create_new_category(db: Session, category_in: CategoryCreate):
    return create_category(db, category_in)


def update_existing_category(db: Session, category_id: int, category_in: CategoryUpdate):
    category = get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="دسته‌بندی یافت نشد")
    return update_category(db, category, category_in)


def remove_category(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="دسته‌بندی یافت نشد")
    delete_category(db, category)
    return True
