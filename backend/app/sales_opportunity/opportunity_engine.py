from app.sales_opportunity.embeddings import customer_embedding
from app.sales_opportunity.similarity_engine import find_similar_customers
from app.sales_opportunity.market_basket import market_basket_analysis
from app.sales_opportunity.graph_engine import build_product_graph, get_related_products
from app.sales_opportunity.ml_repurchase_model import predict_repurchase
from app.sales_opportunity.opportunity_score import calculate_opportunity_score
from app.analytics.customer_metrics import (
    get_customer_last_purchase,
    get_customer_lifetime_value,
    get_churn_risk
)


def generate_advanced_opportunity(db, customer_id, last_product_id, model, all_vectors, transactions):
    last_purchase = get_customer_last_purchase(db, customer_id)
    total_spent = get_customer_lifetime_value(db, customer_id)
    churn_risk = get_churn_risk(db, customer_id)

    # Embedding
    vec = customer_embedding(total_spent, churn_risk, 60)

    # Similar customers
    similar = find_similar_customers(vec, all_vectors)

    # Market Basket
    pairs = market_basket_analysis(transactions)
    G = build_product_graph(pairs)
    related_products = get_related_products(G, last_product_id)

    # ML repurchase prediction
    repurchase_prob = predict_repurchase(model, vec)

    # Final score
    score = calculate_opportunity_score(repurchase_prob, churn_risk, total_spent)

    return {
        "customer_id": customer_id,
        "repurchase_probability": repurchase_prob,
        "similar_customers": similar,
        "related_products": related_products,
        "opportunity_score": score
    }
