from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import get_password_hash
from app.schemas.user import UserCreate


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user_in: UserCreate) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
        password_hash=get_password_hash(user_in.password),
        role_id=user_in.role_id,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
