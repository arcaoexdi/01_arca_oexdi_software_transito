# 🚀 Backend de Gestión de Trámites

Este proyecto implementa un **backend en FastAPI** para manejar clientes, servicios, productos y facturas.  
Incluye integración con **SQLAlchemy**, **Alembic** para migraciones y documentación automática con **Swagger UI**.

---

## 📂 Estructura del proyecto

BackEnd_FastApi/ │── base/ │ └── database.py # Configuración de la base de datos y sesión │── clients/ │ ├── models.py # Modelos SQLAlchemy (Client, Address) │ ├── schemas.py # Schemas Pydantic │ ├── crud.py # Operaciones CRUD │ └── router.py # Endpoints FastAPI │── services/ │ └── models.py │── products/ │ └── models.py │── facture/ │ └── models.py │── migrations/ # Migraciones Alembic │── main.py # Punto de entrada FastAPI │── requirements.txt # Dependencias del proyecto └── README.md # Documentación del proyecto

Código

---

## ⚙️ Tecnologías usadas

- **Lenguaje:** Python 3.12  
- **Framework:** FastAPI  
- **ORM:** SQLAlchemy  
- **Migraciones:** Alembic  
- **Servidor:** Uvicorn  
- **Base de datos:** SQLite (puede migrarse a PostgreSQL/MySQL)  

---

## ▶️ Cómo correr el servidor

1. Activa tu entorno virtual:
   ```bash
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
Instala dependencias:

bash
pip install -r requirements.txt
Ejecuta el servidor:

bash
uvicorn main:app --reload
Accede a la documentación interactiva:

Swagger UI → http://127.0.0.1:8000/docs

OpenAPI JSON → http://127.0.0.1:8000/openapi.json

🗄️ Migraciones con Alembic
Cada vez que modifiques tus modelos (models.py):

Genera una nueva migración:

bash
alembic revision --autogenerate -m "descripcion del cambio"
Aplica la migración:

bash
alembic upgrade head
Revertir la última migración:

bash
alembic downgrade -1
Ver historial:

bash
alembic history
📦 Actualizar dependencias (requirements.txt)
Instala nuevas librerías con pip install nombre_libreria.

Actualiza el archivo requirements.txt:

bash
pip freeze > requirements.txt
Para replicar el entorno en otra máquina:

bash
pip install -r requirements.txt
✅ Buenas prácticas
Mantener los routers separados por dominio (clients, services, etc.).

Usar schemas Pydantic para validación de datos.

Centralizar la configuración de la base en database.py.

Documentar cada modelo y endpoint.

En desarrollo puedes borrar tramites.db y recrear tablas.

En producción siempre usar Alembic para migraciones.

📌 Arquitectura del sistema
text
                ┌───────────────────────────┐
                │         Frontend           │
                │   (Node.js / React / Vue) │
                └─────────────┬─────────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │         FastAPI            │
                │   Routers (Clients, etc.) │
                └─────────────┬─────────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │        SQLAlchemy          │
                │   Models + CRUD + Schemas │
                └─────────────┬─────────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │        Base de datos       │
                │   SQLite / PostgreSQL /    │
                │   MySQL (según entorno)    │
                └───────────────────────────┘
📌 Próximos pasos
Conectar este backend con un frontend en Node.js/React.

Implementar autenticación y autorización (JWT).

Migrar la base de datos a PostgreSQL para producción.