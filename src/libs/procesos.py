from os import path
from src.libs.utils import wait, element_exists, element_view, is_complete_load, convert
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from src.libs.files import create_file, own_dir, delete_file
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from src.libs.interface import Certificate, DateFind
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from time import time

def driver_init():
    # Inicializar el driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.page_load_strategy = 'normal'
    driver = Chrome(
        service = ChromeService(ChromeDriverManager().install()),
        options = chrome_options
      )
    return driver

def login(driver, user: Certificate):
  driver.get("https://portalcfdi.facturaelectronica.sat.gob.mx/")
  try:
    if not element_view(driver, (By.ID, "buttonFiel")):
      raise ValueError('No se ha cargado el elemento')
    buttonFiel = driver.find_element(By.ID, "buttonFiel")
    ActionChains(driver) \
      .click(buttonFiel) \
      .perform()
    # is_complete_load(driver)
    wait()
    # if not element_exists(driver, (By.ID, "fileCertificate")):
    #   print('no se ha cargado el elemento')
    #   raise ValueError('No se ha cargado el elemento')
    fileCertificate = driver.find_element(By.ID, "fileCertificate")
    print(fileCertificate.is_displayed())
    file_path = own_dir()
    create_file(user.certificate, f'{user.instance}.cer')
    create_file(user.key, f'{user.instance}.key')
    fileCertificate.send_keys(path.join(file_path, f'{user.instance}.cer'))
    filePrivateKey = driver.find_element(By.ID, "filePrivateKey")
    filePrivateKey.send_keys(path.join(file_path, f'{user.instance}.key'))
    txtPassword = driver.find_element(By.ID, 'privateKeyPassword')
    txtPassword.send_keys(user.password)
    wait(10)
    buttonSubmit = driver.find_element(By.ID, 'submit')
    ActionChains(driver) \
      .click(buttonSubmit) \
      .perform()
  except ValueError as error:
    print(error)
    raise error
  finally:
    delete_file(f'{user.instance}.cer')
    delete_file(f'{user.instance}.key')


def issued(driver, body: DateFind):
  try:
    is_complete_load(driver)
    optionClick = driver.find_element(By.XPATH, '//a[@href="ConsultaEmisor.aspx"]')
    optionClick.click()
    is_complete_load(driver)
    optionClick = driver.find_element(By.ID, 'ctl00_MainContent_RdoFechas')
    optionClick.click()
    wait()
    driver.execute_script(f"updateDateField('ctl00$MainContent$CldFechaInicial2$Calendario_text', '{body.fechaInicio}');")
    driver.execute_script(f"updateDateField('ctl00$MainContent$CldFechaFinal2$Calendario_text', '{body.fechaFin}');")
    wait(2)
    tipoComprobante = driver.find_element(By.ID, 'ctl00_MainContent_DdlEstadoComprobante')
    seleccionado = Select(tipoComprobante)
    seleccionado.select_by_value('0')
    wait(2)
    btnBuscar = driver.find_element(By.ID, 'ctl00_MainContent_BtnBusqueda')
    btnBuscar.click()
    wait()
    # DivContenedor
    # ContenedorDinamico
    contenidoBusqueda = driver.find_element(By.ID, "ContenedorDinamico")
    contenido = contenidoBusqueda.get_attribute("innerHTML")
    with open("contenido.html", "w", encoding="utf-8") as archivo:
      archivo.write(contenido)
    response = convert(contenidoBusqueda)
    return response
  # wait(10)
  except ValueError as error:
    raise (error)

def prueba_tiempo(driver):
  # url = 'https://www.blackberry.com/la/es'
  url = 'https://www.claro.com.ec'
  driver.get(url)
  try:
    inicio = time()
    if element_exists(driver, (By.CLASS_NAME, 'cyber-card')):
      print('Elemento encontrado')
    else:
      print('Elemento no se ha cargado')
  except:
    print('Error al iniciar sesion')
  finally:
    fin = time()
    print('Tiempo de ejecucion: ', fin - inicio)


def logout(driver):
  btnExit = driver.find_element(By.ID, 'anchorClose')
  ActionChains(driver) \
    .click(btnExit) \
    .perform()