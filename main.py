from fastapi import FastAPI
from src.routers import index
from config.settings import settings

# Crear una instancia de la aplicación FastAPI
app = FastAPI(
    title=settings.app_name,
    version="1.0",
    debug=settings.debug,
    docs_url="/docs",  # Personaliza la URL de la documentación
    redoc_url="/redoc",  # Personaliza la URL de la documentación de ReDoc
)

# Agregar el enrutador APIRouter al punto de montaje
app.include_router(index.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    # Ejecutar la aplicación con Uvicorn en el puerto especificado en las configuraciones
    uvicorn.run(app, host="0.0.0.0", port=8000)