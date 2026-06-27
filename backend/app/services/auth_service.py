from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.core.security import verify_password
from app.core.jwt import create_access_token
from app.repositories.user_repo import get_user_by_username


def authenticate_user(db: Session, username: str, password: str):
    # 1) پیدا کردن کاربر
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="نام کاربری یا رمز عبور اشتباه است."
        )
    print("password =", password)
    print("password len =", len(password))

    print("hash =", user.password_hash)
    print("hash len =", len(user.password_hash))
    print(type(password))
    print(type(user.password_hash))
    # 2) بررسی پسورد
    if not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="نام کاربری یا رمز عبور اشتباه است."
        )

    # 3) بررسی فعال بودن کاربر
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="کاربر غیرفعال است."
        )

    # 4) نقش کاربر (حل مشکل اصلی)
    # اگر نقش نداشت، مقدار پیش‌فرض "user" قرار می‌گیرد
    role_name = user.role.name if user.role else "user"

    # 5) ساخت توکن
    access_token = create_access_token(
        data={
            "user_id": user.id,
            "username": user.username,
            "role": role_name
        }
    )

    return access_token, user
