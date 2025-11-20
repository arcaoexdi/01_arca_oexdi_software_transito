from fastapi import FastAPI
from clients.router import router as clients_router
from services.router import router as services_router
from products.router import router as products_router
from facture.router import router as facture_router

app = FastAPI()


app.include_router(clients_router, prefix="/clients", tags=["Clients"])
app.include_router(services_router, prefix="/services", tags=["Services"])
app.include_router(products_router, prefix="/products", tags=["Products"])
app.include_router(facture_router, prefix="/factures", tags=["Factures"])
