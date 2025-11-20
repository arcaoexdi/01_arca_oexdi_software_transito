from sqlalchemy.orm import Session
from facture.models import Factura
from services.models import Service
from products.models import Product
from clients.models import Client

def create_feature(db: Session, client: Client, servicio: Service = None, productos: list[Product] = None):
    valor_total = 0.0

    if servicio:
        valor_total += servicio.valor

    if productos:
        for producto in productos:
            valor_total += producto.valor

    factura = Factura(
        client_id=client.id,
        service_id=servicio.id if servicio else None,
        products=productos if productos else [],
        valor_total=valor_total
    )

    db.add(factura)
    db.commit()
    db.refresh(factura)
    return factura
