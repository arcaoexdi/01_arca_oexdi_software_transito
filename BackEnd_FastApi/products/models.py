from sqlalchemy import Column, Integer, String, Float, DateTime
from base.database import Base
import datetime

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    stock = Column(Integer, default=0)
    datetime_created = Column(DateTime, default=datetime.datetime.utcnow)