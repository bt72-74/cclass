def build_query(intent: str, params: dict = None):
    if intent == "sales_report":
        return {"type": "sales_summary"}

    if intent == "profit_report":
        return {"type": "profit_summary"}

    if intent == "customer_report":
        return {"type": "customer_info", "customer_id": params.get("customer_id")}

    if intent == "forecast":
        return {"type": "forecast", "model": params.get("model", "prophet")}

    if intent == "alerts":
        return {"type": "alerts", "customer_id": params.get("customer_id")}

    return {"type": "unknown"}
