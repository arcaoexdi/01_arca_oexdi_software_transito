from sqlalchemy.orm import Session
from services.models import Service

def create_service(db: Session, service: Service):
    db.add(service)
    db.commit()
    db.refresh(service)
    return service