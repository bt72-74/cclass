def detect_intent(message: str):
    msg = message.lower()

    if "فروش" in msg or "sales" in msg:
        return "sales_report"

    if "سود" in msg or "profit" in msg:
        return "profit_report"

    if "مشتری" in msg or "customer" in msg:
        return "customer_report"

    if "پیش بینی" in msg or "forecast" in msg:
        return "forecast"

    if "هشدار" in msg or "alert" in msg:
        return "alerts"

    return "unknown"
