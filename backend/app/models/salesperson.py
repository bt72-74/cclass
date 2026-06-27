from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base


class SalesPerson(Base):
    __tablename__ = "salespersons"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True)
    name = Column(String(200), nullable=False)
    phone = Column(String(50))
    email = Column(String(100))

    is_active = Column(Boolean, default=True)
