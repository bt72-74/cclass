from sqlalchemy.orm import Session
from app.ai_copilot.analysis_orchestrator import process_message


def copilot_chat(db: Session, message: str, params: dict = None):
    return process_message(db, message, params)
