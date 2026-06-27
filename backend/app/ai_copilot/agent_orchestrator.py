from app.ai_copilot.agent_router import route_to_agent
from app.ai_copilot.agent_sales import sales_agent
from app.ai_copilot.agent_customer import customer_agent
from app.ai_copilot.agent_forecast import forecast_agent
from app.ai_copilot.agent_alerts import alerts_agent


def run_agents(db, message, params):
    agent = route_to_agent(message)
    params = params or {}

    if agent == "sales":
        return sales_agent(db, message)

    if agent == "customer":
        return customer_agent(db, message, params.get("customer_id"))

    if agent == "forecast":
        return forecast_agent(db, message)

    if agent == "alerts":
        return alerts_agent(db, message, params.get("customer_id"))

    return {"error": "Unknown request"}
