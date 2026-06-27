from pydantic import BaseModel
from datetime import datetime
from typing import List


class SaleItemBase(BaseModel):
    product_id: int
    quantity: float
    unit_price: float
    cost_price: float


class SaleItemCreate(SaleItemBase):
    pass


class SaleItemRead(SaleItemBase):
    id: int
    line_amount: float
    line_profit: float

    class Config:
        orm_mode = True


class SaleBase(BaseModel):
    customer_id: int
    salesperson_id: int
    invoice_date: datetime | None = None


class SaleCreate(SaleBase):
    items: List[SaleItemCreate]


class SaleRead(SaleBase):
    id: int
    invoice_number: str
    total_amount: float
    total_cost: float
    total_profit: float
    status: str
    items: List[SaleItemRead]

    class Config:
        orm_mode = True
