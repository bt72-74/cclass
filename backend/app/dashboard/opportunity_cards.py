from app.sales_opportunity.opportunity_engine import generate_advanced_opportunity


def get_opportunity_card(db, customer_id, model, vectors, transactions):
    opp = generate_advanced_opportunity(db, customer_id, None, model, vectors, transactions)
    return {
        "title": "فرصت فروش مشتری",
        "score": opp["opportunity_score"],
        "repurchase_probability": opp["repurchase_probability"],
        "related_products": opp["related_products"]
    }
