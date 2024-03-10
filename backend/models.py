from sqlalchemy import Boolean, Column, Integer, Float, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)


class Sales(Base):
    __tablename__ = "sales"

    year = Column(Integer, primary_key=True, index=True)
    department = Column(String, primary_key=True, index=True)
    sales = Column(Float)