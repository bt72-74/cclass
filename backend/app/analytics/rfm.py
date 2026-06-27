import pandas as pd
from datetime import datetime


def calculate_rfm(sales_df: pd.DataFrame):
    """
    sales_df columns:
    customer_id, invoice_date, total_amount
    """

    now = datetime.utcnow()

    rfm = sales_df.groupby("customer_id").agg({
        "invoice_date": lambda x: (now - x.max()).days,
        "invoice_number": "count",
        "total_amount": "sum"
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]

    # نمره‌دهی 1 تا 5
    rfm["R_Score"] = pd.qcut(rfm["Recency"], 5, labels=[5,4,3,2,1])
    rfm["F_Score"] = pd.qcut(rfm["Frequency"], 5, labels=[1,2,3,4,5])
    rfm["M_Score"] = pd.qcut(rfm["Monetary"], 5, labels=[1,2,3,4,5])

    rfm["RFM_Score"] = rfm["R_Score"].astype(int) * 100 + \
                       rfm["F_Score"].astype(int) * 10 + \
                       rfm["M_Score"].astype(int)

    return rfm
