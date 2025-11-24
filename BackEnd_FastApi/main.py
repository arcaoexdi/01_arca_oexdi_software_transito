from fastapi import FastAPI
from clients.router import router as clients_router
from services.router import router as services_router
from products.router import router as products_router
from facture.router import router as facture_router

# Import database and models
from base.database import Base, engine
# Import models so they are registered with Base
import services.models
import clients.models
import products.models
import facture.models


# Main FastAPI application
app = FastAPI()

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(clients_router, prefix="/clients", tags=["Clients"])
app.include_router(services_router, prefix="/services", tags=["Services"])
app.include_router(products_router, prefix="/products", tags=["Products"])
app.include_router(facture_router, prefix="/factures", tags=["Factures"])
