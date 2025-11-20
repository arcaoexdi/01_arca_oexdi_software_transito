from sqlalchemy.orm import Session
from clients.models import Client

def create_client(db: Session, client: Client):
    if not client:
        create_client = Client()
        db.add(create_client)
        db.commit()
        db.refresh(create_client)
        return create_client
    return client