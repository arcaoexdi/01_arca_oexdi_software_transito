from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum
from typing import Optional, List

# -------------------------------
# ESQUEMAS DE CLIENTES
# -------------------------------

# Enumeracion para tipos de documento
class TypeDocumentEnum(str, Enum):
    CC = "CC"
    CE = "CE"
    TI = "TI"
    PA = "PA"
    NIT = "NIT"

# Esquema base para Cliente (campos comunes)
class ClientBase(BaseModel):
    # Campos comunes para Cliente
    type_document: TypeDocumentEnum
    number_document: str
    name: str
    last_name: Optional[str] = None
    email: EmailStr
    phone: str

# Esquema para crear Cliente
class ClientCreate(ClientBase):
    pass

# Esquemas de Direccion
class AddressBase(BaseModel):
    # Campos comunes para Direccion
    city: str
    state: str
    zip_code: str

# Esquema para actualizar Cliente
class ClientUpdate(BaseModel):
    type_document: Optional[TypeDocumentEnum] = None
    number_document: Optional[str] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    addresses: Optional[List[AddressBase]] = None

# Esquema de salida para Direccion
class AddressOut(AddressBase):
    id: int
    class Config:
        from_attributes = True

# Esquema de salida para Cliente incluyendo direcciones
class ClientOut(ClientBase):
    # Campos adicionales
    id: int
    type_document: TypeDocumentEnum
    number_document: str
    name: str
    last_name: Optional[str] = None
    email: EmailStr
    phone: str
    datetime_created: datetime
    addresses: List[AddressOut] = []
    
    # Clase de configuracion para permitir conversion desde atributos del modelo ORM
    class Config:
        from_attributes = True

# Esquema para eliminar Cliente por Id
class ClientDelete(BaseModel):
    id: int
