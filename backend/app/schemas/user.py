from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str
    role_id: int


class UserRead(UserBase):
    id: int
    is_active: bool
    role_id: int

    class Config:
        orm_mode = True
