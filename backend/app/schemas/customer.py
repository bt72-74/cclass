from pydantic import BaseModel


class CustomerBase(BaseModel):
    code: str
    name: str
    phone: str | None = None
    email: str | None = None
    city: str | None = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    is_active: bool = True
    segment_id: int | None = None


class CustomerRead(CustomerBase):
    id: int
    is_active: bool
    segment_id: int | None

    class Config:
        orm_mode = True
