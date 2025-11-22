from sqlalchemy.orm import Session
from clients.models import Client

# CRUD operations for Client

# Create a new client
def create_client(db: Session, client: Client):
    if not client:
        create_client = Client()
        db.add(create_client)
        db.commit()
        db.refresh(create_client)
        return create_client
    return client

# Get a client by ID
def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

# Update a client
def update_client(db: Session, client_id: int, updated_data: Client):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        for key, value in updated_data.__dict__.items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
        return client
    return None

# Delete a client
def delete_client(db: Session, client_id: int):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        db.delete(client)
        db.commit()
        return True
    return False
    return False
