def calculate_salesperson_score(sales, profit, new_customers, conversion_rate, retention_rate):
    return (
        0.40 * sales +
        0.25 * profit +
        0.15 * new_customers +
        0.10 * conversion_rate +
        0.10 * retention_rate
    )
