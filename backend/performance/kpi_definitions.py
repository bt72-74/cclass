def get_salesperson_kpis(db, salesperson_id):
    from app.models.sale import Sale
    from sqlalchemy import func

    total_sales = db.query(func.sum(Sale.total_amount))\
        .filter(Sale.salesperson_id == salesperson_id).scalar() or 0

    total_profit = db.query(func.sum(Sale.total_profit))\
        .filter(Sale.salesperson_id == salesperson_id).scalar() or 0

    invoice_count = db.query(func.count(Sale.id))\
        .filter(Sale.salesperson_id == salesperson_id).scalar() or 0

    avg_invoice = total_sales / invoice_count if invoice_count else 0

    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "invoice_count": invoice_count,
        "avg_invoice": avg_invoice
    }
