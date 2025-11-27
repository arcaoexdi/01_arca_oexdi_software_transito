# Librerias importadas para la definicion de los modelos de los clientes en la base de datos.

# Importamos las librerias para la difnicion de los atributos de los modelos
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
# Importamos la libreria para definir la relacion entre modelos
from sqlalchemy.orm import relationship
# Importamos la libreria para la creacion de la tablas de la base de datos
from base.database import Base
# Importamos la libreria para manejar el formato de fechas y horas
import datetime
# Importamos la libreria para definir la enumaracion de tipos de documento o datos que sean necesarios
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

# Modelo de Cliente
class Client(Base):
    # La tabla se va a llamar "clients" en la base de datos
    __tablename__ = "clients"

    # Definimos los campos o atribtuos de la tabla clients
    id = Column(Integer, primary_key=True, index=True)
    
    type_document = Column(Enum(TypeDocumentEnum), nullable=False, index=True) # Relacionados con la clase TypeDocumentEnum
    
    number_document = Column(String(30), unique=True, index=True, nullable=False)
    
    name = Column(String(100), nullable=False, index=True)
    
    last_name = Column(String(100), nullable=True)
    
    email = Column(String(100), unique=True, index=True, 
    nullable=False)
    
    phone = Column(String(20), unique=True, index=True, nullable=False)
    
    datetime_created = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    # Relacion uno a muchos con la tabla Address
    addresses = relationship(
        "Address",
        back_populates="client",
        cascade="all, delete-orphan"
    )

# Creacion de modelo para la direccion del cliente
class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    
    street = Column(String(150), nullable=False)
    
    city = Column(String(100), nullable=False)
    
    state = Column(String(100), nullable=False)
    
    zip_code = Column(String(20), nullable=False)
    
    # Relacion muchos a uno con la tabla Client
    client = relationship("Client", back_populates="addresses")
