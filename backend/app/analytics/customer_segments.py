def map_segment(rfm_score: int) -> str:
    if rfm_score >= 555:
        return "Platinum"
    if rfm_score >= 444:
        return "Gold"
    if rfm_score >= 333:
        return "Silver"
    return "Bronze"
