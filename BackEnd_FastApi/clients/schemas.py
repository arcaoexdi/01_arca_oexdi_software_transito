# SCHEMAS.PY — Versión Mejorada

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
import enum

# ---------------------------------------
# ENUMERACIÓN PARA TIPOS DE DOCUMENTO
# ---------------------------------------

class TypeDocumentEnum(enum.Enum):
    CC = "CC"
    CE = "CE"
    TI = "TI"
    PA = "PA"
    NIT = "NIT"


# ---------------------------------------
# ADDRESS SCHEMAS
# ---------------------------------------

class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


class AddressOut(AddressBase):
    id: int

    class Config:
        from_attributes = True


# ---------------------------------------
# CLIENT SCHEMAS
# ---------------------------------------

class ClientBase(BaseModel):
    type_document: TypeDocumentEnum
    number_document: str
    name: str
    last_name: Optional[str] = None
    email: EmailStr
    phone: str


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    type_document: Optional[TypeDocumentEnum] = None
    number_document: Optional[str] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    addresses: Optional[List[AddressBase]] = None


class ClientOut(ClientBase):
    id: int
    datetime_created: datetime
    is_active: bool
    delete_reason: Optional[str] = None
    addresses: List[AddressOut] = []

    class Config:
        from_attributes = True


class ClientDelete(BaseModel):
    delete_reason: Optional[str] = "Deleted manually"
