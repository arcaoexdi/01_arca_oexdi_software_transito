from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from base.database import SessionLocal
from clients import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/clients/", response_model=schemas.ClientOut)
def create_client_endpoint(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    new_client = crud.create_client(db=db, client_data=client)
    if not new_client:
        raise HTTPException(status_code=400, detail="Client already exists")
    return new_client

@router.get("/clients/{client_id}", response_model=schemas.ClientOut)
def read_client_endpoint(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db=db, client_id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/clients/{client_id}", response_model=schemas.ClientOut)
def update_client_endpoint(client_id: int, updated_client: schemas.ClientUpdate, db: Session = Depends(get_db)):
    client = crud.update_client(db=db, client_id=client_id, updated_data=updated_client)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.delete("/clients/{client_id}", response_model=schemas.ClientOut)
def delete_client_endpoint(client_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_client(db=db, client_id=client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Client not found")
    return deleted
