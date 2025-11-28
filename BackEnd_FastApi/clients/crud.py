# CRUD.PY — Versión Mejorada

from sqlalchemy.orm import Session
from sqlalchemy import or_
from clients.models import Client, Address
from clients.schemas import ClientCreate, ClientUpdate, ClientDelete
from typing import Optional

# ---------------------------------------
# CREAR CLIENTE
# ---------------------------------------

def create_client(db: Session, client_data: ClientCreate) -> Client:

    existing = db.query(Client).filter(
        or_(
            Client.number_document == client_data.number_document,
            Client.email == client_data.email,
            Client.phone == client_data.phone
        )
    ).first()

    if existing:
        raise ValueError("Client already exists")

    new_client = Client(**client_data.dict())

    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return new_client


# ---------------------------------------
# OBTENER CLIENTE
# ---------------------------------------

def get_client(db: Session, client_id: int) -> Optional[Client]:
    return db.query(Client).filter(Client.id == client_id, Client.is_active == True).first()


# ---------------------------------------
# ACTUALIZAR CLIENTE
# ---------------------------------------

def update_client(db: Session, client_id: int, updated_data: ClientUpdate) -> Optional[Client]:

    client = get_client(db, client_id)
    if not client:
        return None

    update_dict = updated_data.dict(exclude_unset=True)

    # Actualizar direcciones
    if "addresses" in update_dict:
        client.addresses = [
            Address(client_id=client.id, **addr.dict())
            for addr in update_dict["addresses"]
        ]
        update_dict.pop("addresses")

    # Validar duplicados al actualizar
    if "email" in update_dict or "phone" in update_dict or "number_document" in update_dict:

        duplicate = db.query(Client).filter(
            Client.id != client.id,
            or_(
                Client.email == update_dict.get("email"),
                Client.phone == update_dict.get("phone"),
                Client.number_document == update_dict.get("number_document")
            )
        ).first()

        if duplicate:
            raise ValueError("Another client already has this email/phone/document.")

    # Aplicar cambios
    for field, value in update_dict.items():
        setattr(client, field, value)

    db.commit()
    db.refresh(client)

    return client


# ---------------------------------------
# ELIMINAR CLIENTE (LÓGICO)
# ---------------------------------------

def delete_client(db: Session, client_id: int, client_delete: ClientDelete) -> Optional[Client]:

    client = get_client(db, client_id)
    if not client:
        return None

    client.is_active = False
    client.delete_reason = client_delete.delete_reason

    db.commit()
    db.refresh(client)

    return client
