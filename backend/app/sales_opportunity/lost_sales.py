from datetime import datetime


def detect_lost_sales(last_purchase_date):
    if not last_purchase_date:
        return True

    days = (datetime.utcnow() - last_purchase_date).days
    return days > 120
