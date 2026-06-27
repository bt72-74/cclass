import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.sale import Sale


def load_sales_dataframe(db: Session):
    rows = db.query(
        func.date(Sale.invoice_date).label("date"),
        func.sum(Sale.total_amount).label("sales")
    ).group_by(
        func.date(Sale.invoice_date)
    ).order_by(
        func.date(Sale.invoice_date)
    ).all()

    df = pd.DataFrame(rows, columns=["date", "sales"])
    df["date"] = pd.to_datetime(df["date"])
    return df
