from sqlalchemy.orm import Session
from services.models import Service

# Crud for Service model operations

# Create a new service
def create_service(db: Session, service: Service):
    db.add(service)
    db.commit()
    db.refresh(service)
    return service

# Acttually the services 
def update_service(db: Session, service_id: int, updated_service: Service):
    service = db.query(Service).filter(Service.id == service_id).first()
    if service:
        service.name = updated_service.name
        service.description = updated_service.description
        service.characteristics = updated_service.characteristics
        service.price = updated_service.price
        db.commit()
        db.refresh(service)
    return service

# Delete the service
def delete_service(db: Session, service_id: int):
    service = db.query(Service).filter(Service.id == service_id).first()
    if service:
        db.delete(service)
        db.commit()
    return service

# Get a service by ID
def get_service(db: Session, service_id: int):
    return db.query(Service).filter(Service.id == service_id).first()
