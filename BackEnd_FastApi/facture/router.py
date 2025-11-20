from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from base.database import SessionLocal
from facture.crud import create_feature
from clients.models import Client
from services.models import Service
from products.models import Product

router = APIRouter()

# Router for Facture operations

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/facturas/")
def create_factura_endpoint(client_id: int, service_id: int = None, product_ids: list[int] = None, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    servicio = db.query(Service).filter(Service.id == service_id).first() if service_id else None
    productos = db.query(Product).filter(Product.id.in_(product_ids)).all() if product_ids else []

    factura = create_factura_endpoint(db, client, servicio, productos)
    return factura
