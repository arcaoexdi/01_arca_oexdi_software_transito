from sqlalchemy.orm import Session
from clients.models import Client, Address
from clients.schemas import ClientCreate, ClientUpdate
from typing import Optional

# -------------------------------
# CRUD OPERATIONS FOR CLIENTS
# -------------------------------

# Create a new client
def create_client(db: Session, client_data: ClientCreate) -> Client:
    existing = db.query(Client).filter(
        (Client.number_document == client_data.number_document) |
        (Client.email == client_data.email) |
        (Client.phone == client_data.phone)
    ).first()
    if existing:
        raise ValueError("Client already exists")
    
    new_client = Client(**client_data.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

# Get a client by ID
def get_client(db: Session, client_id: int) -> Optional[Client]:
    return db.query(Client).filter(Client.id == client_id).first()

# Update a client
def update_client(db: Session, client_id: int, updated_data: ClientUpdate) -> Optional[Client]:
    client = get_client(db, client_id)
    if not client:
        return None

    update_dict = updated_data.dict(exclude_unset=True)
    
    # Validation duplicates if unique fields are updated
    if "addresses" in update_dict:
        client.addresses = [Address(**addr) for addr in update_dict["addresses"]]
        update_dict.pop("addresses")

    # Update the rest of the fields
    for field, value in update_dict.items():
        setattr(client, field, value)

    db.commit()
    db.refresh(client)
    return client

# Delete a client
def delete_client(db: Session, client_id: int) -> Optional[Client]:
    client = get_client(db, client_id)
    if not client:
        return None

    db.delete(client)
    db.commit()
    return client
