from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from base.database import Base
import datetime


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name_client = Column(String, index=True)
    document = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    datetime_created = Column(DateTime, default=datetime.datetime.utcnow)

class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)

    client = relationship("Client", back_populates="addresses")
Client.addresses = relationship("Address", order_by=Address.id, back_populates="client")