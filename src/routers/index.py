from fastapi import APIRouter, Depends
from config.settings import settings
from typing import List
from src.libs.files import own_dir
from src.libs.interface import DataClient
from src.libs.procesos import driver_init, login, prueba_tiempo, issued

# Crear una instancia del enrutador APIRouter
router = APIRouter()

# Ruta para obtener información de la aplicación
@router.get("/info")
async def get_app_info():
    return {"app_name": settings.app_name, "version": "1.0"}

# Ruta para listar elementos (ejemplo)
@router.get("/items/", response_model=List[str])
async def list_items(skip: int = 0, limit: int = 10):
    items = ["item1", "item2", "item3", "item4", "item5"]
    return items[skip : skip + limit]

# Ruta para obtener un elemento por su ID (ejemplo)
@router.get("/items/{item_id}")
async def get_item(item_id: int):
    items = {"1": "item1", "2": "item2", "3": "item3", "4": "item4", "5": "item5"}
    if str(item_id) in items:
        return {"item_id": item_id, "name": items[str(item_id)]}
    return {"error": "Item not found"}

# Ruta protegida que requiere autenticación (ejemplo)
# @router.get("/secure/")
# async def secure_route(current_user: dict = Depends(get_current_user)):
#     return {"message": "This is a secure route", "user": current_user}

@router.post('/issued')
async def issued(req: DataClient):
  try:
    driver = driver_init()
    login(driver, req)
    response = issued(driver,req)
    driver.close()
    driver.quit()
    return { "data": response }
  except ValueError as error:
    return { "message": error}
  # finally:
  #    driver.close()
  #    driver.quit()

@router.get('/test')
async def test():
    browser = driver_init()
    prueba_tiempo(browser)
    return { "content": 'test'}


@router.get('/ruta')
async def ruta():
  return { "content": own_dir()}