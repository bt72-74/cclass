from app.analytics.customer_metrics import (
    get_customer_lifetime_value,
    get_customer_last_purchase,
    get_churn_risk
)


def customer_agent(db, message: str, customer_id: int):
    return {
        "type": "customer",
        "lifetime_value": get_customer_lifetime_value(db, customer_id),
        "last_purchase": get_customer_last_purchase(db, customer_id),
        "churn_risk": get_churn_risk(db, customer_id)
    }
