from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from base.database import SessionLocal
from services import crud, schemas, models

# Router for service endpoints 

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new service
@router.post("/services/", response_model=schemas.ServiceOut)
def create_service_endpoint(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    new_service = crud.create_service(db=db, service_data=service)
    if not new_service:
        raise HTTPException(status_code=400, detail="Service already exists")
    return new_service

# Get a service by ID
@router.get("/services/{service_id}", response_model=schemas.ServiceOut)
def read_service(service_id: int, db: Session = Depends(get_db)):
    service = crud.get_service(db=db, service_id=service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

# Update a service
@router.put("/services/{service_id}", response_model=schemas.ServiceOut)
def update_service_endpoint(service_id: int, updated_service: schemas.ServiceUpdate, db: Session = Depends(get_db)):
    service = crud.update_service(db=db, service_id=service_id, updated_data=crud.update_service(db, service_id, models.Service(**updated_service.dict())))
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

# Delete a service
@router.delete("/services/{service_id}")
def delete_service_endpoint(service_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_service(db=db, service_id=service_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"message": "Service deleted successfully"}
