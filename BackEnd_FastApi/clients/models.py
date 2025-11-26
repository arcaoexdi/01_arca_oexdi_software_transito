# Librerias importadas para la definicion de los modelos de los clientes en la base de datos.

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from base.database import Base
import datetime
import enum

# -------------------------------
# MODELOS PARA CLIENTES
# -------------------------------

# Enumeracion para tipos de documento
class TypeDocumentEnum(enum.Enum):
    CC = "CC"
    CE = "CE"
    TI = "TI"
    PA = "PA"
    NIT = "NIT"

# Modelo para Cliente
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    type_document = Column(Enum(TypeDocumentEnum), nullable=False, index=True)
    number_document = Column(String(30), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False, index=True)
    last_name = Column(String(100), nullable=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone = Column(String(20), unique=True, index=True, nullable=False)
    datetime_created = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    addresses = relationship(
        "Address",
        back_populates="client",
        cascade="all, delete-orphan"
    )

# Modelo para Direccion
class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    street = Column(String(150), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    zip_code = Column(String(20), nullable=False)

    client = relationship("Client", back_populates="addresses")
