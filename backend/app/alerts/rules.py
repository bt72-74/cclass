def low_sales_rule(sales_today: float, threshold: float = 1000000):
    return sales_today < threshold


def low_profit_rule(profit_today: float, threshold: float = 300000):
    return profit_today < threshold


def churn_risk_rule(churn_risk: int, threshold: int = 70):
    return churn_risk >= threshold


def low_stock_rule(stock_qty: int, threshold: int = 10):
    return stock_qty <= threshold
