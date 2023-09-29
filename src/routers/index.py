from fastapi import APIRouter, Depends
from config.settings import settings
from typing import List
from src.libs.interface import DataClient
from src.libs.procesos import driver_init, login, logout, issued, received

# Crear una instancia del enrutador APIRouter
router = APIRouter()

# Ruta para obtener información de la aplicación
@router.get("/info")
async def get_app_info():
  return {"app_name": settings.app_name, "version": "1.0"}

@router.post('/issued')
async def emitidos(req: DataClient):
  try:
    driver = driver_init()
    login(driver, req)
    response = issued(driver, req)
    logout(driver)
    driver.close()
    driver.quit()
    print(response)
    return { "data": response }
  except ValueError as error:
    return { "message": error}
  # finally:
  #    driver.close()
  #    driver.quit()

@router.post('/received')
async def recibidos(req: DataClient):
  try:
    driver = driver_init()
    login(driver, req)
    response = received(driver, req)
    logout(driver)
    driver.close()
    driver.quit()
    return { "data": response }
  except ValueError as error:
    return { "message": error}
  # finally:
  #    driver.close()
  #    driver.quit()