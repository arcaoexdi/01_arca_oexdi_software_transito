from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from base.database import SessionLocal
from facture.crud import create_feature
from clients.models import Client
from services.models import Service
from products.models import Product

router = APIRouter()

# Router for Product operations

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/products/")
def create_product_endpoint(client_id: int, service_id: int = None, product_ids: list[int] = None, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    service_id = db.query(Service).filter(Service.id == service_id).first() if service_id else None
    product_ids = db.query(Product).filter(Product.id.in_(product_ids)).all() if product_ids else []

    product = create_feature(db, client, service_id, product_ids)
    return product