from fastapi import APIRouter
from config.settings import settings
from typing import List
from src.libs.firmas import principal, secundario
from src.libs.procesos import driver_init

# Crear una instancia del enrutador APIRouter
router = APIRouter()

@router.get('/cliente')
async def cliente():
  try:
    driver = driver_init()
    principal(driver)
    driver.close()
    driver.quit()
    return { 'message': 'Correcto' }
  except ValueError as error:
    return { "message": error}
  # finally:
  #    driver.close()
  #    driver.quit()

@router.get('/local')
async def local():
  driver = driver_init()
  secundario(driver)
  driver.close()
  driver.quit()


