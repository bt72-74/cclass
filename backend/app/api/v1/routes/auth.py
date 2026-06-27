from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import Token
from app.services.auth_service import authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])


from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login", response_model=Token)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    access_token, user = authenticate_user(db, request.username, request.password)
    return Token(access_token=access_token)
