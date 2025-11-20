from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from base.database import Base
import datetime

# Tabla intermedia para relación muchos-a-muchos entre Factura y Productos
factura_productos = Table(
    "factura_productos",
    Base.metadata,
    Column("factura_id", Integer, ForeignKey("facturas.id")),
    Column("product_id", Integer, ForeignKey("products.id"))
)

class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, index=True)

    client_id = Column(Integer, ForeignKey("clients.id"))
    service_id = Column(Integer, ForeignKey("services.id"), nullable=True)

    # Valor total de la factura (servicio + productos)
    valor_total = Column(Float)

    fecha = Column(DateTime, default=datetime.datetime.utcnow)

    # Relaciones ORM
    client = relationship("Client")
    service = relationship("Service")
    products = relationship("Product", secondary=factura_productos)
