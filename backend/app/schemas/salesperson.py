from pydantic import BaseModel
from typing import Optional


class SalesPersonBase(BaseModel):
    code: str
    name: str
    phone: str | None = None
    email: str | None = None


class SalesPersonCreate(SalesPersonBase):
    pass


class SalesPersonUpdate(SalesPersonBase):
    is_active: bool = True


class SalesPersonRead(SalesPersonBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class SalesPersonPerformance(BaseModel):
    id: int
    code: str
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    is_active: bool
    total_sales: float
    total_profit: float
    invoice_count: int
    profit_margin_percent: float

    class Config:
        orm_mode = True
