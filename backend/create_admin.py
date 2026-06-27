# create_admin.py

from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.security import get_password_hash
from app.models.user import User
from app.models.role import Role


def create_admin_user():
    db: Session = SessionLocal()

    # 1) بررسی وجود نقش admin
    role = db.query(Role).filter(Role.name == "admin").first()
    if not role:
        print("🔧 نقش admin پیدا نشد. در حال ساخت...")
        role = Role(name="admin")
        db.add(role)
        db.commit()
        db.refresh(role)
        print("✅ نقش admin ساخته شد.")

    # 2) بررسی وجود کاربر admin
    user = db.query(User).filter(User.username == "admin").first()
    if user:
        print("ℹ️ کاربر admin از قبل وجود دارد.")
        return

    print("🔧 در حال ساخت کاربر admin ...")

    admin_user = User(
        username="admin",
        email="admin@example.com",
        password_hash=get_password_hash("admin"),  # پسورد: admin
        is_active=True,
        role_id=role.id
    )

    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)

    print("✅ کاربر admin با موفقیت ساخته شد.")
    print("👤 username: admin")
    print("🔑 password: admin")


if __name__ == "__main__":
    create_admin_user()
