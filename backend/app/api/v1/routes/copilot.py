from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional

from app.core.database import get_db
from app.ai_copilot.copilot_service import copilot_chat


router = APIRouter(prefix="/copilot", tags=["AI Copilot"])


class CopilotRequest(BaseModel):
    message: str
    params: Optional[dict] = None


@router.post("/chat")
def copilot_chat_endpoint(request: CopilotRequest, db: Session = Depends(get_db)):
    return copilot_chat(db, request.message, request.params)
