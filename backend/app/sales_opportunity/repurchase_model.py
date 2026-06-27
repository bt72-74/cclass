from datetime import datetime


def repurchase_probability(last_purchase_date):
    if not last_purchase_date:
        return 0

    days = (datetime.utcnow() - last_purchase_date).days

    if days <= 30:
        return 90
    if days <= 60:
        return 70
    if days <= 120:
        return 40
    return 10
