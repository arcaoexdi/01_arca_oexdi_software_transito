from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from base.database import SessionLocal
from clients import crud, schemas, models

# Router for client endpoints 

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new client
@router.post("/clients/", response_model=schemas.ClientOut)
def create_client_endpoint(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    new_client = crud.create_client(db=db, client=models.Client(**client.dict()))
    if not new_client:
        raise HTTPException(status_code=400, detail="Client already exists")
    return new_client

# Get a client by ID
@router.get("/clients/{client_id}", response_model=schemas.ClientOut)
def read_client_endpoint(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db=db, client_id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

# Update a client
@router.put("/clients/{client_id}", response_model=schemas.ClientOut)
def update_client_endpoint(client_id: int, updated_client: schemas.ClientUpdate, db: Session = Depends(get_db)):
    client = crud.update_client(db=db, client_id=client_id, updated_data=crud.update_client(db, client_id, models.Client(**updated_client.dict())))
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

# Delete a client
@router.delete("/clients/{client_id}")
def delete_client_endpoint(client_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_client(db=db, client_id=client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"}