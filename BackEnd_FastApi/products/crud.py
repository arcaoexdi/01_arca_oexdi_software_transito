from sqlalchemy.orm import Session
from facture.models import Factura
from services.models import Service
from products.models import Product

def create_product(db: Session, product: Product, service: Service = None, products: list[Product] = None):
    valor_total = 0.0

    if service:
        valor_total += service.valor

    if products:
        for product in products:
            valor_total += product.valor

    factura = Factura(
        service_id=service.id if service else None,
        products=products if products else [],
        valor_total=valor_total
    )

    db.add(factura)
    db.commit()
    db.refresh(factura)
    return factura
