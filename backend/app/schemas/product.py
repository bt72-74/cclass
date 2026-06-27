from pydantic import BaseModel


class ProductBase(BaseModel):
    code: str
    name: str
    category_id: int
    brand_id: int
    cost_price: float
    sale_price: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    is_active: bool = True


class ProductRead(ProductBase):
    id: int
    margin_percent: float
    is_active: bool

    class Config:
        orm_mode = True
