from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from base.database import SessionLocal
from clients.models import Service

router = APIRouter()

# Router for Client operations

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/services/")
def create_service_endpoint(service_id: int, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()
    
    if not service:
        return {"error": "Service not found"}
    