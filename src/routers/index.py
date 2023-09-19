from fastapi import APIRouter, Depends
from config.settings import settings
from typing import List
from src.libs.files import own_dir
from src.libs.interface import DataClient
from src.libs.procesos import driver_init, login, logout, prueba_tiempo, issued

# Crear una instancia del enrutador APIRouter
router = APIRouter()

# Ruta para obtener información de la aplicación
@router.get("/info")
async def get_app_info():
    return {"app_name": settings.app_name, "version": "1.0"}

@router.post('/issued')
async def recibidos(req: DataClient):
  try:
    driver = driver_init()
    login(driver, req)
    response = issued(driver, req)
    logout(driver)
    driver.close()
    driver.quit()
    return { "data": response }
  except ValueError as error:
    return { "message": error}
  # finally:
  #    driver.close()
  #    driver.quit()
