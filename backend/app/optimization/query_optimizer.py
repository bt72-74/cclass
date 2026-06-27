from sqlalchemy.orm import joinedload


def optimize_sales_query(query):
    return query.options(
        joinedload("items"),
        joinedload("customer"),
        joinedload("salesperson")
    )
