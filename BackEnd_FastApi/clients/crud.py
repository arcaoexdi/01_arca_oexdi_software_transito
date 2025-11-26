# Librerias importadas para las operaciones CRUD de los clientes.

# Libreria sqlalchemy para la gestion de sesiones
from sqlalchemy.orm import Session
# Libreria del modelo de Cliente y Direccion
from clients.models import Client, Address
# Libreria de los esquemas de Cliente
from clients.schemas import ClientCreate, ClientUpdate
# Libreria para tipos opcionales
from typing import Optional

# -------------------------------
# CRUD PARA CLIENTES
# -------------------------------

# Crear un nuevo cliente
def create_client(db: Session, client_data: ClientCreate) -> Client:
    # Validar si el cliente ya existe por numero de documento, email o telefono
    existing = db.query(Client).filter(
        (Client.number_document == client_data.number_document) |
        (Client.email == client_data.email) |
        (Client.phone == client_data.phone)
    ).first()
    # Si el cliente ya existe, se emite un aviso de error de que el cliente ya existe
    if existing:
        raise ValueError("Client already exists")
    
    # Si el cliente no existe, se crea uno nuevo
    new_client = Client(**client_data.dict())
    # Se agrega el nuevo cliente a la base de datos
    db.add(new_client)
    # Se confirma la transaccion
    db.commit()
    # Se actualiza la instancia del cliente con los datos de la base de datos
    db.refresh(new_client)
    # Se retorna el nuevo cliente creado
    return new_client

# Obtener un cliente por ID unico
def get_client(db: Session, client_id: int) -> Optional[Client]:
    # Se retorna el cliente con el ID especificado
    return db.query(Client).filter(Client.id == client_id).first()

# Actualizar un cliente
def update_client(db: Session, client_id: int, updated_data: ClientUpdate) -> Optional[Client]:
    # Se obtiene el cliente por ID unico
    client = get_client(db, client_id)
    # Si el cliente no existe, crear uno nuevo
    if not client:
        # Crear un nuevo cliente con los datos actualizados
        create = create_client(db, ClientCreate(**updated_data.dict(exclude_unset=True)))
        # Se retorna el cliente creado
        return create
    # Convertir los datos actualizados a un diccionario excluyendo los valores no establecidos
    update_dict = updated_data.dict(exclude_unset=True)
    
    # Validar duplicados si se actualizan campos únicos
    if "addresses" in update_dict:
        client.addresses = [Address(**addr) for addr in update_dict["addresses"]]
        update_dict.pop("addresses")

    # Actualizar el resto de los campos
    for field, value in update_dict.items():
        setattr(client, field, value)

    # Confirmar la transaccion
    db.commit()
    # Actualizar la instancia del cliente con los datos de la base de datos
    db.refresh(client)
    # Retornar el cliente actualizado
    return client

# Eliminar un cliente
def delete_client(db: Session, client_id: int) -> Optional[Client]:
    # Obtener el cliente por ID unico
    client = get_client(db, client_id)
    # Si el cliente no existe, retornar None
    if not client:
        # No se encontró el cliente
        return None
    # Eliminar el cliente de la base de datos
    db.delete(client)
    # Confirmar la transaccion
    db.commit()
    # Retornar el cliente eliminado
    return client
