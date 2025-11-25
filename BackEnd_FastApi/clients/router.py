from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from base.database import get_db
from clients import crud, schemas

# -------------------------------
# ROUTER FOR CLIENTS
# -------------------------------

# Clients router
router = APIRouter(prefix="/clients", tags=["Clients"])

# Create a new client
@router.post("/", response_model=schemas.ClientOut)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_client(db=db, client_data=client)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Read a client by ID
@router.get("/{client_id}", response_model=schemas.ClientOut)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db=db, client_id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

# Update a client
@router.put("/{client_id}", response_model=schemas.ClientOut)
def update_client(client_id: int, updated_client: schemas.ClientUpdate, db: Session = Depends(get_db)):
    try:
        client = crud.update_client(db=db, client_id=client_id, updated_data=updated_client)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return client
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Delete a client
@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_client(db=db, client_id=client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"detail": "Client deleted successfully"}
