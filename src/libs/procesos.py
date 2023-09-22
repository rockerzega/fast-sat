from os import path
from src.libs.interface import Tipo
from selenium.webdriver import Chrome
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from src.libs.interface import Certificate, DateFind
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from src.libs.files import create_file, own_dir, delete_file
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from src.libs.utils import wait, element_exists, element_view, is_complete_load, convert

def driver_init():
    # Inicializar el driver
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--start-maximized')
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
  except NoSuchElementException:
    raise ValueError('No se ha cargado el elemento')  
  except ValueError as error:
    print(error)
    raise error
  finally:
    delete_file(f'{user.instance}.cer')
    delete_file(f'{user.instance}.key')


def issued(driver, body: DateFind):
  try:
    is_complete_load(driver)
    wait()
    curr = 'https://portalcfdi.facturaelectronica.sat.gob.mx/'
    if driver.current_url != curr:
      raise ValueError('El servicio sat no se encentra disponible')
    optionClick = driver.find_element(By.XPATH, '//a[@href="ConsultaEmisor.aspx"]')
    optionClick.click()
    is_complete_load(driver)
    if not element_exists(driver, (By.ID, 'ctl00_MainContent_RdoFechas')):
      raise ValueError('No se ha cargado el elemento')
    wait()
    # optionClick = driver.find_element(By.ID, 'ctl00_MainContent_RdoFechas')
    # optionClick.click()
    driver.execute_script("document.getElementById('ctl00_MainContent_RdoFechas').click()")
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
    contentResult = driver.find_element(By.ID, 'ctl00_MainContent_PnlResultados')
    if not contentResult.is_displayed():
      print('no tiene datos')
      return []
    # DivContenedor
    # ContenedorDinamico
    contenidoBusqueda = driver.find_element(By.ID, "ContenedorDinamico")
    # contenido = contenidoBusqueda.get_attribute("innerHTML")
    # with open("contenido.html", "w", encoding="utf-8") as archivo:
    #   archivo.write(contenido)
    response = convert(contenidoBusqueda, Tipo.issued)
    return response
  # wait(10)
  except ValueError as error:
    return [{"message": f'Error: {str(error)}'}]

def received(driver, body: DateFind):
  response = []
  ultimo = datetime.strptime(body.fechaInicio , '%d/%m/%Y')
  try:
    is_complete_load(driver)
    wait()
    curr = 'https://portalcfdi.facturaelectronica.sat.gob.mx/'
    if driver.current_url != curr:
      raise ValueError('El servicio sat no se encentra disponible')
    optionClick = driver.find_element(By.XPATH, '//a[@href="ConsultaReceptor.aspx"]')
    optionClick.click()
    is_complete_load(driver)
    if not element_exists(driver, (By.ID, 'ctl00_MainContent_RdoFechas')):
      raise ValueError('No se ha cargado el elemento')
    wait()
    optionClick = driver.find_element(By.ID, 'ctl00_MainContent_RdoFechas')
    optionClick.click()
    # driver.execute_script("document.getElementById('ctl00_MainContent_RdoFechas').click()")
    wait(5)
    fechaInicio = ultimo
    iteraciones = datetime.strptime(body.fechaFin, '%d/%m/%Y') - fechaInicio
    for i in range(iteraciones.days + 1):
      actual = fechaInicio + timedelta(days=i)
      ultimo = actual
      fecha = actual.strftime("%d/%m/%Y").split('/')
      if actual.year != datetime.now().year:
        selAnio = driver.find_element(By.ID, 'DdlAnio')
        selecAnio = Select(selAnio)
        selecAnio.select_by_value(str(int(fecha[2])))
      selMes = driver.find_element(By.ID, 'ctl00_MainContent_CldFecha_DdlMes')
      selecMes = Select(selMes)
      selecMes.select_by_value(str(int(fecha[1])))
      selDia = driver.find_element(By.ID, 'ctl00_MainContent_CldFecha_DdlDia')
      selecDia = Select(selDia)
      selecDia.select_by_value(str(int(fecha[0])))
      wait()
      if i == 0:
        selStatus = driver.find_element(By.ID, 'ctl00_MainContent_DdlEstadoComprobante')
        selecStatus = Select(selStatus)
        selecStatus.select_by_value('0')
        wait(2)
      btnBuscar = driver.find_element(By.NAME, 'ctl00$MainContent$BtnBusqueda')
      btnBuscar.click()
      wait()
      contentResult = driver.find_element(By.ID, 'ctl00_MainContent_PnlResultados')
      if not contentResult.is_displayed():
        print('no tiene datos')
        pass
      # DivContenedor
      # ContenedorDinamico
      contenidoBusqueda = driver.find_element(By.ID, "ContenedorDinamico")
      # contenido = contenidoBusqueda.get_attribute("innerHTML")
      # with open("contenido.html", "w", encoding="utf-8") as archivo:
      #   archivo.write(contenido)
      response.extend(convert(contenidoBusqueda, Tipo.received))
    return response
  except ValueError as error:
    return response.append({"message": str(error), "ultimaFecha": ultimo})
  
def logout(driver):
  btnExit = driver.find_element(By.ID, 'anchorClose')
  ActionChains(driver) \
    .click(btnExit) \
    .perform()