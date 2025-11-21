from sqlalchemy.orm import Session
from services.models import Service
from services.schemas import ServiceCreate, ServiceUpdate
from typing import Optional

# CRUD operations for Service model

# Create a new service
def create_service(db: Session, service_data: ServiceCreate) -> Optional[Service]:
    """
    Create a new service in the database.
    Validates if a service with the same name already exists.
    Returns the created Service object or None if duplicate.
    """
    existing = db.query(Service).filter(Service.name == service_data.name).first()
    if existing:
        return None  # Duplicate found

    new_service = Service(**service_data.dict())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service


# Get a service by ID
def get_service(db: Session, service_id: int) -> Optional[Service]:
    """
    Retrieve a service by its ID.
    Returns the Service object or None if not found.
    """
    return db.query(Service).filter(Service.id == service_id).first()


# Update a service
def update_service(db: Session, service_id: int, updated_data: ServiceUpdate) -> Optional[Service]:
    """
    Update an existing service by ID.
    Returns the updated Service object or None if not found.
    """
    service = get_service(db, service_id)
    if not service:
        return None

    for field, value in updated_data.dict().items():
        setattr(service, field, value)

    db.commit()
    db.refresh(service)
    return service


# Delete a service
def delete_service(db: Session, service_id: int) -> Optional[Service]:
    """
    Delete a service by ID.
    Returns the deleted Service object or None if not found.
    """
    service = get_service(db, service_id)
    if not service:
        return None

    db.delete(service)
    db.commit()
    return service
