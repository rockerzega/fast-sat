from time import sleep
from random import randint
from src.libs.interface import Tipo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait(seconds = 0):
  if seconds == 0:
    seconds = randint(2, 6)
  sleep(seconds)

def element_exists(driver, element, waiting = 10) -> bool:
  try:
    WebDriverWait(driver, waiting).until(EC.presence_of_element_located(element))
  except:
    return False
  return True

def element_view(driver, element, waiting=10) -> bool:
  try:
    WebDriverWait(driver, waiting).until(EC.visibility_of_element_located(element))
  except:
    return False
  return True

def is_complete_load(driver, waiting=10):
  try:
    WebDriverWait(driver, waiting).until(
      lambda driver: driver.execute_script('return document.readyState') == 'complete'
    )
    print('La pagina esta cargada completamente')
  except ValueError as error:
    raise f'No se ha logrado cargar la página: {error}'

KEYS = [
  'folio',
  'RFCEmisor',
  'emisor',
  'RFCReceptor',
  'receptor',
  'fechaEmision',
  'fechaCertificacion',
  'pac',
  'total',
  'tipoComprobante',
  'estadoCancelacion',
  'estadoComprobante',
  'estatusProcesoCancelacion',
  'fechaCancelacion',
  'RFCTerceros',
  'motivo',
  'folioSustitcion'
]

def convert(content, tipo: Tipo):
  data = []
  try :
    inicio = 5 if tipo == Tipo.issued else 1
    table = content.find_elements(By.XPATH, "//*[@id='ctl00_MainContent_tblResult']/tbody/child::tr")
    for rows in table[1:]:
      elemento = {}
      items = rows.find_elements(By.TAG_NAME, 'span')
      i = 0
      for item in items[inicio:]:
        elemento[KEYS[i]] = item.text
        i = i + 1
      data.append(elemento)

    # Convertimos a JSON
    # data = json.dumps(data, indent=2, ensure_ascii=False)
  except Exception as error:
    print(f'Se ha producido un error: {str(error)}')
  finally:
    return data
