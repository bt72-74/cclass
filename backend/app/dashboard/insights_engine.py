def generate_insights(kpis):
    insights = []

    if kpis["sales_today"] < (kpis["sales_month"] / 30):
        insights.append("فروش امروز کمتر از میانگین ماه است.")

    if kpis["profit_today"] < (kpis["profit_month"] / 30):
        insights.append("سود امروز کمتر از میانگین ماه است.")

    if kpis["sales_month"] > 1.2 * kpis["profit_month"]:
        insights.append("حاشیه سود نسبت به فروش پایین است.")

    return insights
