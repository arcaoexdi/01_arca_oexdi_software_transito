from pydantic import BaseModel
from datetime import datetime

# Schemas of Service

class ServiceBase(BaseModel):
    name: str
    description: str
    characteristics: str
    price: float

class ServiceCreate(ServiceBase):
    pass  # no incluye datetime_created

class ServiceUpdate(ServiceBase):
    pass

class ServiceOut(ServiceBase):
    id: int
    datetime_created: datetime  # se devuelve como datetime válido

    class Config:
        orm_mode = True
