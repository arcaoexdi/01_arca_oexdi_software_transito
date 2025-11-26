# La documentacion se hara en español y las variables, funciones y clases se nombraran en ingles.
# Este archivo configura la conexion a la base de datos, la sesion y la declaracion base para SQLAlchemy.
# Tambien incluye instrucciones para manejar migraciones con Alembic.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# -------------------------------
# MOTOR DE BASE DE DATOS
# -------------------------------
# Cambia la URL según el motor:
# - SQLite: "sqlite:///./tramites.db"
# - PostgreSQL: "postgresql://user:password@localhost/dbname"
# - MySQL: "mysql+pymysql://user:password@localhost/dbname"
SQLALCHEMY_DATABASE_URL = "sqlite:///./tramites.db"

# Crear el motor de la base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necesario solo para SQLite
)

# -------------------------------
# SESION DE LA BASE DE DATOS
# -------------------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# -------------------------------
# DECLARACION DE LA BASE
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
# IMPORTAR MODELOS DE LOS MÓDULOS
# -------------------------------
# Importar aquí asegura que Alembic y Base conozcan todos los modelos.
import clients.models
import services.models
import products.models
import facture.models

# -------------------------------
# MIGRACIONES ALEMBIC
# -------------------------------
# Flujo de trabajo:
# 1. Revision del historial de migraciones
# 1.1. alembic history --verbose
# 2. Revision del estado actual de la base de datos
# 2.1. alembic current
# 3. Aplicar migraciones pendientes
# 3.1. alembic upgrade head
# 4. alembic revision --autogenerate -m "Mensaje"
# 5. alembic downgrade -1
#
# Nota: target_metadata = Base.metadata en env.py
