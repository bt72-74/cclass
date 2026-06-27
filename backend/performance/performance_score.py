def calculate_performance_score(kpis, max_values):
    score = (
        0.5 * normalize(kpis["total_sales"], max_values["total_sales"]) +
        0.3 * normalize(kpis["total_profit"], max_values["total_profit"]) +
        0.2 * normalize(kpis["invoice_count"], max_values["invoice_count"])
    )
    return round(score, 2)
