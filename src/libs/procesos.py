from os import path
from src.libs.utils import wait
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from src.libs.files import create_file, own_dir
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from src.libs.interface import Certificate, DataClient
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def driver_init():
    # Inicializar el driver
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.page_load_strategy = 'normal'
    driver = Chrome(
        service = ChromeService(ChromeDriverManager().install()),
        options = chrome_options
      )
    return driver

def login(driver, user: Certificate):
  driver.get("https://portalcfdi.facturaelectronica.sat.gob.mx/")
  buttonFiel = driver.find_element(By.ID, "buttonFiel")
  # wait_until_element_visible(buttonFiel)
  wait(5)
  # buttonFiel.click()
  ActionChains(driver) \
    .click(buttonFiel) \
    .perform()
  # is_complete_load(driver)
  wait(10)
  fileCertificate = driver.find_element(By.ID, "fileCertificate")
  print('FileCertificate is visible? : ', fileCertificate.is_displayed())
  # wait_until_element_visible(fileCertificate)
  # is_visible(driver, fileCertificate)
  file_path = own_dir()
  print(file_path)
  create_file(user.certificate, 'UME200911GE5.cer')
  create_file(user.key, 'UME200911GE5.key')
  fileCertificate.send_keys(path.join(file_path, 'UME200911GE5.cer'))
  filePrivateKey = driver.find_element(By.ID, "filePrivateKey")
  filePrivateKey.send_keys(path.join(file_path, 'UME200911GE5.key'))
  txtPassword = driver.find_element(By.ID, 'privateKeyPassword')
  txtPassword.send_keys(user.password)
  buttonSubmit = driver.find_element(By.ID, 'submit')
  ActionChains(driver) \
    .click(buttonSubmit) \
    .perform()


def issued(driver, body: DataClient):
  print('esta es la data que ha llegado')
  print(type(body.fechaInicio), ' : fechaInicio : ', body.fechaInicio )
  print(type(body.fechaFin), ' : fechaFin : ', body.fechaFin)
  optionClick = driver.find_element(By.XPATH, '//a[@href="ConsultaEmisor.aspx"]')
  is_complete_load(driver)
  is_visible(driver, optionClick)
  optionClick.click()
  wait(5)
  optionClick = driver.find_element(By.ID, 'ctl00_MainContent_RdoFechas')
  wait_until_element_visible(optionClick)
  optionClick.click()
  wait(5)
  driver.execute_script(f"updateDateField('ctl00$MainContent$CldFechaInicial2$Calendario_text', '{body.fechaInicio}');")
  driver.execute_script(f"updateDateField('ctl00$MainContent$CldFechaFinal2$Calendario_text', '{body.fechaFin}');")
  wait(2)
  tipoComprobante = driver.find_element(By.ID, 'ctl00_MainContent_DdlEstadoComprobante')
  seleccionado = Select(tipoComprobante)
  seleccionado.select_by_value('0')
  wait(2)
  btnBuscar = driver.find_element(By.ID, 'ctl00_MainContent_BtnBusqueda')
  btnBuscar.click()
  wait(10)
  # DivContenedor
  # ContenedorDinamico
  contenidoBusqueda = driver.find_element(By.ID, "ContenedorDinamico")
  contenido = contenidoBusqueda.get_attribute("innerHTML")
  with open("contenido.html", "w", encoding="utf-8") as archivo:
    archivo.write(contenido)
  response = convert(contenidoBusqueda)
  return response
  # wait(10)