from selenium.webdriver import Chrome
from src.libs.utils import wait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from src.libs.interface import Certificate

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
  wait(5)
  fileCertificate = driver.find_element(By.ID, "fileCertificate")
  print('FileCertificate is visible? : ', fileCertificate.is_displayed())
  # wait_until_element_visible(fileCertificate)
  # is_visible(driver, fileCertificate)
  wait(20)
  fileCertificate.send_keys("/home/rockerzega/files/UME200911GE5.cer")
  filePrivateKey = driver.find_element(By.ID, "filePrivateKey")
  filePrivateKey.send_keys("/home/rockerzega/files/UME200911GE5.key")
  txtPassword = driver.find_element(By.ID, 'privateKeyPassword')
  txtPassword.send_keys(user.password)
  wait(5)
  buttonSubmit = driver.find_element(By.ID, 'submit')
  ActionChains(driver) \
    .click(buttonSubmit) \
    .perform()
