from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# -------------------------------
# DATABASE ENGINE
# -------------------------------
# Cambia la URL según el motor:
# - SQLite: "sqlite:///./tramites.db"
# - PostgreSQL: "postgresql://user:password@localhost/dbname"
# - MySQL: "mysql+pymysql://user:password@localhost/dbname"
SQLALCHEMY_DATABASE_URL = "sqlite:///./tramites.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necesario solo para SQLite
)

# -------------------------------
# SESSION MANAGEMENT
# -------------------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# -------------------------------
# DECLARATIVE BASE
# -------------------------------
Base = declarative_base()

# -------------------------------
# DEPENDENCY FOR FASTAPI ENDPOINTS
# -------------------------------
def get_db():
    """Crea y cierra sesión automáticamente en endpoints FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------
# IMPORT MODELS
# -------------------------------
# Importar aquí asegura que Alembic y Base conozcan todos los modelos.
import clients.models
import services.models
import products.models
import facture.models

# -------------------------------
# ALEMBIC MIGRATIONS
# -------------------------------
# Flujo de trabajo:
# 1. alembic revision --autogenerate -m "Mensaje"
# 2. alembic upgrade head
# 3. alembic downgrade -1
#
# Nota: target_metadata = Base.metadata en env.py
