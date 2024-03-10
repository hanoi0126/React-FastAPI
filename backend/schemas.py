from pydantic import BaseModel

class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class SalesBase(BaseModel):
    year: int
    department: str
    sales: float


class SalesCreate(SalesBase):
    pass


class Sales(SalesBase):
    class Config:
        orm_mode = True