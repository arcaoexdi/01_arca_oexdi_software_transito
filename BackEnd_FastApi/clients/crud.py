from sqlalchemy.orm import Session
from clients.models import Client
from clients.schemas import ClientCreate, ClientUpdate
from typing import Optional
from clients.models import TypeDocumentEnum as ModelEnum
from clients.schemas import TypeDocumentEnum as SchemaEnum

# Mapping function between schema enum and model enum
def map_type_document(schema_value: SchemaEnum) -> ModelEnum:
    mapping = {
        SchemaEnum.CC: ModelEnum.CC,
        SchemaEnum.CE: ModelEnum.CE,
        SchemaEnum.TI: ModelEnum.TI,
        SchemaEnum.PA: ModelEnum.PA,
        SchemaEnum.NIT: ModelEnum.NIT,
    }
    return mapping[schema_value]

# Create a new client
def create_client(db: Session, client_data: ClientCreate) -> Optional[Client]:
    existing = db.query(Client).filter(
        (Client.number_document == client_data.number_document) |
        (Client.email == client_data.email) |
        (Client.phone == client_data.phone)
    ).first()
    if existing:
        return None
    
    data_dict = client_data.dict()
    data_dict['type_document'] = map_type_document(client_data.type_document)

    new_client = Client(**data_dict)
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

    update_dict = updated_data.dict(exclude_unset=True, exclude={"id", "datetime_created"})
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
