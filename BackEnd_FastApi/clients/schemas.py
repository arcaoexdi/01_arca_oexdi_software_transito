from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum
from typing import Optional, List

# -------------------------------
# SCHEMAS FOR CLIENTS
# -------------------------------

# Enum for type of documents (same as in models)
class TypeDocumentEnum(str, Enum):
    CC = "CC"
    CE = "CE"
    TI = "TI"
    PA = "PA"
    NIT = "NIT"

# Base schema for Client (common fields)
class ClientBase(BaseModel):
    type_document: TypeDocumentEnum
    number_document: str
    name: str
    last_name: Optional[str] = None
    email: EmailStr
    phone: str

# Schema for creating Client
class ClientCreate(ClientBase):
    pass

# Schemas of Address
class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

# Schema for updating Client
class ClientUpdate(BaseModel):
    type_document: Optional[TypeDocumentEnum] = None
    number_document: Optional[str] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    addresses: Optional[List[AddressBase]] = None

# Output schema for Address
class AddressOut(AddressBase):
    id: int
    class Config:
        from_attributes = True

# Output schema for Client including addresses
class ClientOut(ClientBase):
    id: int
    datetime_created: datetime
    addresses: List[AddressOut] = []

    class Config:
        from_attributes = True

# Delete schema for Id client
class ClientDelete(BaseModel):
    id: int
