from sqlalchemy import Column, Integer, String, Float, DateTime
from base.database import Base
from datetime import datetime

# Define the Service model for the services table

class Service(Base):
    __tablename__ = "services"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    characteristics = Column(String, index=True)
    price = Column(Float)
    datetime_created = Column(DateTime, default=datetime.utcnow)