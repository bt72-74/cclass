from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True)
    name = Column(String(200), nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"))
    brand_id = Column(Integer, ForeignKey("brands.id"))

    cost_price = Column(Float, nullable=False)
    sale_price = Column(Float, nullable=False)
    margin_percent = Column(Float, nullable=False)

    is_active = Column(Boolean, default=True)

    category = relationship("Category")
    brand = relationship("Brand")
