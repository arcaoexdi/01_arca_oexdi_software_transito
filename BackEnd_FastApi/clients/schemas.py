from pydantic import BaseModel
from datetime import datetime
from enum import Enum

# Enum for type of documents (same as in models)
class TypeDocumentEnum(str, Enum):
    CC = "cedula de ciudadania"
    CE = "cedula de extranjeria"
    TI = "tarjeta de identidad"
    PA = "pasaporte"
    NIT = "nit"

# Base schema for Client (common fields)
class ClientBase(BaseModel):
    name: str
    last_name: str
    type_document: TypeDocumentEnum
    number_document: str
    email: str
    phone: str

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    name: str | None = None
    last_name: str | None = None
    type_document: TypeDocumentEnum | None = None
    number_document: str | None = None
    email: str | None = None
    phone: str | None = None

# Schemas of Address
class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class AddressOut(AddressBase):
    id: int
    class Config:
        from_attributes = True

class ClientOut(ClientBase):
    id: int
    datetime_created: datetime
    addresses: list[AddressOut] = []

    class Config:
        from_attributes = True

class ClientDelete(BaseModel):
    id: int
