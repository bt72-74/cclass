from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String(50), unique=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    salesperson_id = Column(Integer, ForeignKey("salespersons.id"))
    invoice_date = Column(DateTime, default=datetime.utcnow)

    total_amount = Column(Float, default=0)
    total_cost = Column(Float, default=0)
    total_profit = Column(Float, default=0)
    status = Column(String(20), default="Paid")  # Paid / Cancelled / Draft

    customer = relationship("Customer")
    salesperson = relationship("SalesPerson")
    items = relationship("SaleItem", back_populates="sale", cascade="all, delete-orphan")
