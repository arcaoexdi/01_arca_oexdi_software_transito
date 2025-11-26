# Librerias importadas para la definicion de las rutas de los clientes en la parte del crud.

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from base.database import get_db
from clients import crud, schemas

# -------------------------------
# RUTAS DE CLIENTES
# -------------------------------

# Clientes router
router = APIRouter(prefix="/clients", tags=["Clients"])

# Crear un nuevo cliente
@router.post("/", response_model=schemas.ClientOut)
# Definimos una funcion para crear un cliente
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    # Intentar crear un nuevo cliente
    try:
        return crud.create_client(db=db, client_data=client)
    # Capturar errores de valor y lanzar excepcion HTTP
    except ValueError as e:
        # Lanzar excepcion HTTP con codigo 400 y detalle del error
        raise HTTPException(status_code=400, detail=str(e))


# Leer un cliente por ID
@router.get("/{client_id}", response_model=schemas.ClientOut)
# Definimos una funcion para leer un cliente por ID
def read_client(client_id: int, db: Session = Depends(get_db)):
    # Obtener el cliente por ID unico
    client = crud.get_client(db=db, client_id=client_id)
    # Si el cliente no existe, lanzar una excepcion HTTP 404
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    # Si el cliente existe, retornarlo
    return client

# Actualizar un cliente
@router.put("/{client_id}", response_model=schemas.ClientOut)
# Definimos una funcion para actualizar un cliente
def update_client(client_id: int, updated_client: schemas.ClientUpdate, db: Session = Depends(get_db)):
    # Intentar actualizar el cliente
    try:
        # Actualizar el cliente con los datos proporcionados
        client = crud.update_client(db=db, client_id=client_id, updated_data=updated_client)
        # Si el cliente no existe despues de la actualizacion, lanzar una excepcion HTTP 404
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        # Retornar el cliente actualizado
        return client
    except ValueError as e:
        # Capturar errores de valor y lanzar excepcion HTTP
        raise HTTPException(status_code=400, detail=str(e))

# Eliminar un cliente
@router.delete("/{client_id}")
# Definimos una funcion para eliminar un cliente
def delete_client(client_id: int, db: Session = Depends(get_db)):
    # Intentar eliminar el cliente
    deleted = crud.delete_client(db=db, client_id=client_id)
    # Si el cliente no existe, lanzar una excepcion HTTP 404
    if not deleted:
        raise HTTPException(status_code=404, detail="Client not found")
    # Retornar un mensaje de exito
    return {"detail": "Client deleted successfully"}
