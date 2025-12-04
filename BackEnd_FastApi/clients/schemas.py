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

# Clases para de direcciones asociadas a clientes
class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

# Clase para salida de direcciones asociadas a clientes
class AddressOut(AddressBase):
    id: int

    class Config:
        from_attributes = True


# ---------------------------------------
# CLIENT SCHEMAS
# ---------------------------------------

# Clases base para clientes
class ClientBase(BaseModel):
    type_document: TypeDocumentEnum
    number_document: str
    name: str
    last_name: Optional[str] = None
    email: EmailStr
    phone: str
    listaddress: Optional[List[AddressBase]] = None

# Clase para creación de clientes el cual hereda de ClientBase
class ClientCreate(ClientBase):
    pass

# Clase para actualización de clientes el cual hereda de ClientBase
class ClientUpdate(BaseModel):
    type_document: Optional[TypeDocumentEnum] = None
    number_document: Optional[str] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    addresses: Optional[List[AddressBase]] = None


# Clase para salida de clientes el cual hereda de ClientBase
class ClientOut(ClientBase):
    id: int
    datetime_created: datetime
    is_active: bool
    delete_reason: Optional[str] = None
    addresses: List[AddressOut] = []

    class Config:
        from_attributes = True


# Clase para eliminación lógica de clientes
class ClientDelete(BaseModel):
    is_active: bool = False
    delete_reason: Optional[str] = "Deleted manually"
