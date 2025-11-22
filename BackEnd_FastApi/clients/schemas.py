from pydantic import BaseModel
from datetime import datetime

# Schemas of Client

class ClientBase(BaseModel):
    name: str
    type_document: str
    number_document: str
    email: str
    phone: str
    addresses: list = []  # List of addresses (can be empty)

class ClientCreate(ClientBase):
    pass  # no incluye datetime_created

class ClientUpdate(ClientBase):
    pass

class ClientOut(ClientBase):
    id: int
    datetime_created: datetime  # is included in output
    
    class Config:
        orm_mode = True
