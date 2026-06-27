def calculate_opportunity_score(repurchase_prob, churn_risk, total_spent):
    score = (
        0.5 * repurchase_prob +
        0.3 * (100 - churn_risk) +
        0.2 * min(total_spent / 1_000_000, 100)
    )
    return round(score, 2)
