from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True)
    name = Column(String(200), nullable=False)
    phone = Column(String(50))
    email = Column(String(100))
    city = Column(String(100))

    segment_id = Column(Integer, ForeignKey("customer_segments.id"))
    segment = relationship("CustomerSegment")

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
