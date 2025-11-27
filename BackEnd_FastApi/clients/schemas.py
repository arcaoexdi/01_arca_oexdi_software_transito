# Libreria pydantic para la definicion de esquemas de datos
from pydantic import BaseModel, EmailStr

# Libreria para la definicion de los formatos de fecha y hora
from datetime import datetime

# Libreria para segmentacion de tipos de datos
from typing import Optional, List

# Libreria para definir la enumaracion de tipos de documento o datos que sean necesarios
import enum

# -------------------------------
# ESQUEMAS DE CLIENTES
# -------------------------------

# Enumeracion para tipos de documento
class TypeDocumentEnum(enum.Enum):
    CC = "CC"
    CE = "CE"
    TI = "TI"
    PA = "PA"
    NIT = "NIT"

# Esquemas de Direccion
class AddressBase(BaseModel):
    # Campos comunes para Direccion
    street: str
    
    city: str
    
    state: str
    
    zip_code: str

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
