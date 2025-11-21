from fastapi import FastAPI
from clients.router import router as clients_router
from services.router import router as services_router
from products.router import router as products_router
from facture.router import router as facture_router

# Import database and models
from base.database import Base, engine
from services import models as service_models
from clients import models as client_models
from products import models as product_models
from facture import models as facture_models

# Main FastAPI application
app = FastAPI()

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(clients_router, prefix="/clients", tags=["Clients"])
app.include_router(services_router, prefix="/services", tags=["Services"])
app.include_router(products_router, prefix="/products", tags=["Products"])
app.include_router(facture_router, prefix="/factures", tags=["Factures"])
