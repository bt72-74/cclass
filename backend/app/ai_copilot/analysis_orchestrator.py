from app.ai_copilot.context_manager import update_context, get_context
from app.ai_copilot.agent_router import route_to_agent
from app.ai_copilot.llm_engine import llm_analyze
from app.ai_copilot.data_access import execute_query


# نگاشت agent به query type
AGENT_QUERY_MAP = {
    "sales": "sales_summary",
    "customer": "customer_info",
    "forecast": "forecast",
    "alerts": "alerts",
    "profit": "profit_summary",
}


def process_message(db, message: str, params: dict = None):
    update_context(message)
    params = params or {}

    # تشخیص موضوع پیام
    agent = route_to_agent(message)

    # واکشی داده‌های مرتبط از دیتابیس
    business_data = None
    if agent in AGENT_QUERY_MAP:
        query = {"type": AGENT_QUERY_MAP[agent], **params}
        try:
            business_data = execute_query(db, query)
        except Exception:
            business_data = None

    # ارسال به Claude با داده‌های واقعی
    answer = llm_analyze(message, business_data)

    return {
        "answer": answer,
        "agent": agent,
        "has_data": business_data is not None,
    }
