from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from base.database import SessionLocal
from clients.models import Client

router = APIRouter()

# Router for Client operations

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/clients/")
def create_client_endpoint(client_id: int, service_id: int = None, product_ids: list[int] = None, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    
    if not client:
        return {"error": "Client not found"}
    