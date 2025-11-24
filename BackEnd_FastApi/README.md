# 🚀 Backend de Gestión de Trámites

Este proyecto implementa un **backend en FastAPI** para manejar clientes, usuarios, servicios, productos y facturas.  

Incluye integración con **SQLAlchemy**, **Alembic** para migraciones y documentación automática con **Swagger UI**.

---

## 📂 Estructura del proyecto
# Configuración de la base de datos y sesión 
BackEnd_FastApi/ 
      │── base/ 
             └── database.py 

# Endpoints FastAPI 
         │── clients/ 
                  └── models.py 
         │── users/ 
                  └── models.py 
         │── services/ │ 
                  └── models.py 
         │── products/ 
                  └── models.py 
         │── facture/ 
                  └── models.py 

# Modelos SQLAlchemy (Client, Users, Services, Products, Facture)
         └── schemas.py 

# Schemas Pydantic (Client, Users, Services, Products, Facture) 
         └── crud.py 
         
# Operaciones CRUD (Client, Users, Services, Products, Facture)
         └── router.py 
         
# Migrations(Client, Users, Services, Products, Facture)
         └── migrations/ 

# Migraciones Alembic 
         └── main.py 

# Punto de entrada FastAPI
         └── requirements.txt 

# Dependencias del proyecto 
         └── README.md 
         
# Documentación del proyecto
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

### 1. Activa tu entorno virtual:
   
- **source venv/bin/activate**   # Linux/Mac
- **venv\Scripts\activate**      # Windows

### 2. Instala dependencias:

- **pip install -r requirements.txt**

###  3. Ejecuta el servidor:

- **uvicorn main:app --reload**

###  4. Accede a la documentación interactiva:

- **Swagger UI → http://127.0.0.1:8000/docs**
- **OpenAPI JSON → http://127.0.0.1:8000/openapi.json**

### 5. 🗄️ Migraciones con Alembic

- Cada vez que se modifiquen los modelos (models.py):

### 6. Genera una nueva migración:

- **alembic revision --autogenerate -m "descripcion del cambio"**

### 7. Aplica la migración:

- **alembic upgrade head**

### 8. Revertir la última migración:

- **alembic downgrade -1**

### 9. Ver historial:
- **alembic history**

### 10. 📦 Actualizar dependencias (requirements.txt)

- **Instala nuevas librerías con pip install nombre_libreria.**

### 11. Actualiza el archivo requirements.txt:

- **pip freeze > requirements.txt**

### 12. Para replicar el entorno en otra máquina:

- **pip install -r requirements.txt**

## ✅ Buenas prácticas
-- **Mantener los routers separados por dominio (clients, services, etc.).**
-- **Usar schemas Pydantic para validación de datos.**
-- **Centralizar la configuración de la base en database.py.**
-- **Documentar cada modelo y endpoint.**
-- **En desarrollo puedes borrar tramites.db y recrear tablas.**

## En producción siempre usar Alembic para migraciones.

📌 Arquitectura del sistema

*                ┌───────────────────────────┐
*                │         Frontend           │
*                │   (Node.js / React / Vue) │
*                └─────────────┬─────────────┘
*                              │
*                              ▼
*                ┌───────────────────────────┐
*                │         FastAPI            │
*                │   Routers (Clients, etc.) │
*                └─────────────┬─────────────┘
*                              │
*                              ▼
*                ┌───────────────────────────┐
*                │        SQLAlchemy          │
*                │   Models + CRUD + Schemas │
*                └─────────────┬─────────────┘
*                              │
*                              ▼
*                ┌───────────────────────────┐
*                │        Base de datos       │
*                │   SQLite / PostgreSQL /    │
*                │   MySQL (según entorno)    │
*                └───────────────────────────┘

### 📌 Próximos pasos
- ***Conectar este backend con un frontend en Node.js/React.***

- ***Implementar autenticación y autorización (JWT).***

- ***Migrar la base de datos a PostgreSQL para producción.***