def route_to_agent(message: str) -> str:
    msg = message.lower()

    if any(w in msg for w in ["فروش", "درآمد", "فاکتور", "sales", "revenue"]):
        return "sales"

    if any(w in msg for w in ["سود", "حاشیه", "profit", "margin"]):
        return "profit"

    if any(w in msg for w in ["مشتری", "customer", "خریدار", "client"]):
        return "customer"

    if any(w in msg for w in ["پیش‌بینی", "پیش بینی", "آینده", "forecast", "predict"]):
        return "forecast"

    if any(w in msg for w in ["هشدار", "alert", "خطر", "ریسک", "warning"]):
        return "alerts"

    # برای سوالات عمومی (سلام، راهنمایی، ...) بدون داده جواب بده
    return "general"
