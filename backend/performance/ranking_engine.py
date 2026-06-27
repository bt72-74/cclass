from app.performance.kpi_definitions import get_salesperson_kpis
from app.performance.performance_score import calculate_performance_score


def rank_salespersons(db, salesperson_ids):
    kpi_map = {}
    max_values = {"total_sales": 0, "total_profit": 0, "invoice_count": 0}

    # جمع‌آوری KPIها
    for sid in salesperson_ids:
        kpis = get_salesperson_kpis(db, sid)
        kpi_map[sid] = kpis

        max_values["total_sales"] = max(max_values["total_sales"], kpis["total_sales"])
        max_values["total_profit"] = max(max_values["total_profit"], kpis["total_profit"])
        max_values["invoice_count"] = max(max_values["invoice_count"], kpis["invoice_count"])

    # محاسبه امتیاز
    ranking = []
    for sid, kpis in kpi_map.items():
        score = calculate_performance_score(kpis, max_values)
        ranking.append({"salesperson_id": sid, "score": score})

    ranking.sort(key=lambda x: x["score"], reverse=True)
    return ranking
