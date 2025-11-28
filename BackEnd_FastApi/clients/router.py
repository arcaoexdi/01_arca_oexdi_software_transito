# ROUTER.PY — Versión Mejorada

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from base.database import get_db
from clients import crud, schemas

router = APIRouter(prefix="/clients", tags=["Clients"])


# ---------------------------------------
# CREATE
# ---------------------------------------

@router.post("/", response_model=schemas.ClientOut)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_client(db=db, client_data=client)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# ---------------------------------------
# READ
# ---------------------------------------

@router.get("/{client_id}", response_model=schemas.ClientOut)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db=db, client_id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


# ---------------------------------------
# UPDATE
# ---------------------------------------

@router.put("/{client_id}", response_model=schemas.ClientOut)
def update_client(client_id: int, updated_client: schemas.ClientUpdate, db: Session = Depends(get_db)):

    try:
        client = crud.update_client(db=db, client_id=client_id, updated_data=updated_client)

        if not client:
            raise HTTPException(status_code=404, detail="Client not found")

        return client

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# ---------------------------------------
# DELETE (LÓGICO)
# ---------------------------------------

@router.delete("/{client_id}", response_model=schemas.ClientOut)
def delete_client(client_id: int, delete_info: schemas.ClientDelete, db: Session = Depends(get_db)):

    deleted = crud.delete_client(db=db, client_id=client_id, client_delete=delete_info)

    if not deleted:
        raise HTTPException(status_code=404, detail="Client not found")

    return deleted
