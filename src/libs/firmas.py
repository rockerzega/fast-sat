from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from src.libs.utils import wait
def principal(driver):  
  try:
    url = 'https://firmas.myprogress.group'
    # url = 'https://arsuite-test.toc.com.ec'
    driver.get(url)
    wait(10)
    driver.find_element(By.CSS_SELECTOR, ".hover\\3A bg-primh").click()
    wait()
    driver.find_element(By.CSS_SELECTOR, ".border-primh > .block").click()
    wait()
    driver.find_element(By.CSS_SELECTOR, ".w-1\\/3").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .block").click()
    wait()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .justify-between").click()
    wait()
    driver.find_element(By.CSS_SELECTOR, ".grid > li .flex").click()
    driver.find_element(By.CSS_SELECTOR, ".next-form").click()
    driver.find_element(By.CSS_SELECTOR, ".text-gray-100").click()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > span > .block > .w-full").click()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > span > .block > .w-full").send_keys("JUAN")
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(1) > div:nth-child(2) .w-full").click()
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(1) > div:nth-child(2) .w-full").send_keys("MAURICIO")
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(1) > div:nth-child(3) .w-full").click()
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(1) > div:nth-child(3) .w-full").send_keys("VILAÑEZ")
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > span > .block > .w-full").click()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > span > .block > .w-full").send_keys("PARRA")
    # driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) .w-full").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) .w-full")
    selector = Select(dropdown)
    # dropdown.find_element(By.XPATH, "//option[. = 'Cédula']").click()
    selector.select_by_value('ci')
    # driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) option:nth-child(1)").click()
    # driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) .w-full").click()
    # driver.find_element(By.CSS_SELECTOR, ".text-gray-700").click()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) .w-full").send_keys("1723729478")
    # --------------------------------------------------------------------------
    driver.find_element(By.CSS_SELECTOR, ".ant-calendar-picker-input").click()
    elemento = driver.find_element(By.CSS_SELECTOR, '.ant-calendar-input')
    elemento.send_keys('1990-05-22')
    # driver.find_element(By.LINK_TEXT, "2023").click()
    # driver.find_element(By.CSS_SELECTOR, ".ant-calendar-year-panel-prev-decade-btn").click()
    # driver.find_element(By.CSS_SELECTOR, ".ant-calendar-year-panel-prev-decade-btn").click()
    # driver.find_element(By.CSS_SELECTOR, ".ant-calendar-year-panel-prev-decade-btn").click()
    # driver.find_element(By.LINK_TEXT, "1990").click()
    # driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > .ant-calendar-cell:nth-child(6) > .ant-calendar-date").click()
    # ---------------------------------------------------------------------------------------------
    calendario = driver.find_element(By.CSS_SELECTOR, 'input.ant-calendar-picker-input')
    calendario.send_keys('1990-05-23')
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(9) .w-full").click()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(9) .w-full").send_keys("0981296193")
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) .w-full").click()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) .w-full").send_keys("test@test.com")
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(12) .w-full").click()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(12) .w-full").send_keys("test@test.com")
    # driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > span .p-2\\.5").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > span .p-2\\.5")
    selector = Select(dropdown)
    selector.select_by_value('Pichincha')
    # dropdown.find_element(By.XPATH, "//option[. = 'Pichincha']").click()
    driver.find_element(By.CSS_SELECTOR, "option:nth-child(19)").click()
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(2) > div:nth-child(2) .w-full").click()
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(2) > div:nth-child(2) .w-full").send_keys("QUITO")
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(2) > div:nth-child(3) .w-full").click()
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(2) > div:nth-child(3) .w-full").send_keys("CHILLOGALLO")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
    checkboxes[1].click()
    # driver.find_element(By.CSS_SELECTOR, ".ant-checkbox-wrapper:nth-child(1) .ant-checkbox-inner").click()
    wait(1)
    driver.execute_script("window.scrollTo(0,1380)")

    element = driver.find_element(By.CSS_SELECTOR, "#signature > canvas")
    # driver.execute_script(
    #   """
    #   const canvas = document.querySelector("#signature > canvas");
    #   const ctx = canvas.getContext("2d");
    #   ctx.beginPath();
    #   ctx.moveTo(10, 10);
    #   ctx.lineTo(100, 100);
    #   ctx.lineTo(150, 10);
    #   ctx.stroke();
    #   """
    # )
    wait(1)
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.CSS_SELECTOR, "#signature > canvas")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "#signature > canvas")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, "#signature > canvas").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > span").click()
    wait(1)
    driver.find_element(By.CSS_SELECTOR, ".mt-5 > .text-white").click()
    element = driver.find_element(By.CSS_SELECTOR, ".text-white")
    print(element.text)
    element.click()
    # driver.find_element(By.CSS_SELECTOR, "b:nth-child(2)").click()
    # driver.find_element(By.CSS_SELECTOR, ".flex-col").click()
    wait(10)  
    # except NoSuchElementException:
    #   raise ValueError('No se ha cargado el elemento')  
  except ValueError as error:
    print(error)
  #   raise error
  # finally:
  #   delete_file(f'{user.instance}.cer')
  #   delete_file(f'{user.instance}.key')

def secundario (driver):
  try:
    driver.get("https://arsuite-test.toc.com.ec/")
    wait(10)
    # 3 | click | css=.hover\3A bg-primh | 
    driver.find_element(By.CSS_SELECTOR, ".hover\\3A bg-primh").click()
    # 4 | click | css=li:nth-child(1) > .border-primh > .block | 
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .border-primh > .block").click()
    wait()
    # 5 | click | css=.w-1\/3 | 
    driver.find_element(By.CSS_SELECTOR, ".w-1\\/3").click()
    # 6 | click | css=li:nth-child(1) .block | 
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .block").click()
    wait()
    # 7 | click | css=div:nth-child(1) > .justify-between | 
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .justify-between").click()
    # 8 | click | css=.grid > li .flex | 
    driver.find_element(By.CSS_SELECTOR, ".grid > li .flex").click()
    # 9 | click | css=.next-form | 
    driver.find_element(By.CSS_SELECTOR, ".next-form").click()
    # 10 | click | css=.text-gray-100 | 
    driver.find_element(By.CSS_SELECTOR, ".text-gray-100").click()
    # 11 | click | css=div:nth-child(1) > span > .block > .w-full | 
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > span > .block > .w-full").click()
    # 12 | type | css=div:nth-child(1) > span > .block > .w-full | LUIS
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > span > .block > .w-full").send_keys("LUIS")
    # 13 | click | css=.grid:nth-child(1) > div:nth-child(2) .w-full | 
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(1) > div:nth-child(2) .w-full").click()
    # 14 | type | css=.grid:nth-child(1) > div:nth-child(2) .w-full | ALBERTO
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(1) > div:nth-child(2) .w-full").send_keys("ALBERTO")
    # 15 | click | css=.grid:nth-child(1) > div:nth-child(3) .w-full | 
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(1) > div:nth-child(3) .w-full").click()
    # 16 | type | css=.grid:nth-child(1) > div:nth-child(3) .w-full | VILAÑEZ
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(1) > div:nth-child(3) .w-full").send_keys("VILAÑEZ")
    # 17 | click | css=div:nth-child(4) > span > .block > .w-full | 
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > span > .block > .w-full").click()
    # 18 | type | css=div:nth-child(4) > span > .block > .w-full | PARRA
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > span > .block > .w-full").send_keys("PARRA")
    # 19 | click | css=div:nth-child(5) .w-full | 
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) .w-full").click()
    # 20 | select | css=div:nth-child(5) .w-full | label=Cédula
    dropdown = driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) .w-full")
    Select(dropdown).select_by_value('ci')
    # 21 | click | css=div:nth-child(5) option:nth-child(1) | 
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) option:nth-child(1)").click()
    # 22 | click | css=div:nth-child(6) .w-full | 
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) .w-full").click()
    # 23 | type | css=div:nth-child(6) .w-full | 1777777777
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) .w-full").send_keys("1777777777")
    # 24 | click | css=.anticon-calendar > svg | 
    driver.find_element(By.CSS_SELECTOR, ".anticon-calendar > svg").click()
    # 25 | type | css=.ant-calendar-input | 1990-05-22
    driver.find_element(By.CSS_SELECTOR, ".ant-calendar-input").send_keys("1990-05-22")
    # 26 | click | css=.min-h-max | 
    driver.find_element(By.CSS_SELECTOR, ".min-h-max").click()
    # 27 | click | css=div:nth-child(9) .w-full | 
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(9) .w-full").click()
    # 28 | type | css=div:nth-child(9) .w-full | 095668734
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(9) .w-full").send_keys("095668734")
    # 29 | click | css=div:nth-child(11) .w-full | 
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) .w-full").click()
    # 30 | type | css=div:nth-child(11) .w-full | rockerzega@hotmail.com
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) .w-full").send_keys("rockerzega@hotmail.com")
    # 31 | click | css=div:nth-child(12) .w-full | 
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(12) .w-full").click()
    # 32 | type | css=.text-gray-700 | rockerzega@hotmal.com
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(12) .w-full").send_keys("rockerzega@hotmail.com")
    # 33 | click | css=div:nth-child(1) > span .p-2\.5 | 
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > span .p-2\\.5").click()
    # 34 | select | css=div:nth-child(1) > span .p-2\.5 | label=Pichincha
    dropdown = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > span .p-2\\.5")
    Select(dropdown).select_by_value('Pichincha')
    # 35 | click | css=option:nth-child(19) | 
    driver.find_element(By.CSS_SELECTOR, "option:nth-child(19)").click()
    # 36 | click | css=.grid:nth-child(2) > div:nth-child(2) .w-full | 
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(2) > div:nth-child(2) .w-full").click()
    # 37 | type | css=.grid:nth-child(2) > div:nth-child(2) .w-full | QUITO
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(2) > div:nth-child(2) .w-full").send_keys("QUITO")
    # 38 | click | css=.grid:nth-child(2) > div:nth-child(3) .w-full | 
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(2) > div:nth-child(3) .w-full").click()
    # 39 | type | css=.grid:nth-child(2) > div:nth-child(3) .w-full | CHILLOGALLO
    driver.find_element(By.CSS_SELECTOR, ".grid:nth-child(2) > div:nth-child(3) .w-full").send_keys("CHILLOGALLO")
    # 40 | click | css=.ant-checkbox-wrapper:nth-child(1) .ant-checkbox-input | 
    driver.find_element(By.CSS_SELECTOR, ".ant-checkbox-wrapper:nth-child(1) .ant-checkbox-input").click()
    wait(1)
     # 41 | mouseDownAt | css=#signature > canvas | 123,132.25
    element = driver.find_element(By.CSS_SELECTOR, "#signature > canvas")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 42 | mouseMoveAt | css=#signature > canvas | 123,132.25
    element = driver.find_element(By.CSS_SELECTOR, "#signature > canvas")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 43 | mouseUpAt | css=#signature > canvas | 123,132.25
    element = driver.find_element(By.CSS_SELECTOR, "#signature > canvas")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 44 | click | css=#signature > canvas | 
    driver.find_element(By.CSS_SELECTOR, "#signature > canvas").click()
    # 45 | mouseDownAt | css=#signature > canvas | 131,93.25
    element = driver.find_element(By.CSS_SELECTOR, "#signature > canvas")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 46 | mouseMoveAt | css=#signature > canvas | 131,93.25
    element = driver.find_element(By.CSS_SELECTOR, "#signature > canvas")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 47 | mouseUpAt | css=#signature > canvas | 131,93.25
    element = driver.find_element(By.CSS_SELECTOR, "#signature > canvas")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 48 | click | css=#signature > canvas | 
    driver.find_element(By.CSS_SELECTOR, "#signature > canvas").click()
    # 49 | click | css=li:nth-child(2) > span | 
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > span").click()
    # 50 | click | css=.mt-5 > .text-white | 
    driver.find_element(By.CSS_SELECTOR, ".mt-5 > .text-white").click()
    # 51 | click | css=.text-white | 
    driver.find_element(By.CSS_SELECTOR, ".text-white").click()
    # 52 | click | xpath=label[contains(., 'Click aquí')] |
    driver.find_element(By.XPATH, "//label[contains(., 'Click aquí')]").click()
    # 53 | upload file | css=input[type="file"]
    file_input_element = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    archivo_a_cargar = '/home/rockerzega/Imágenes/aprobado.jpg'
    file_input_element.send_keys(archivo_a_cargar)
    wait(40)
  except Exception as err:
    print('error: ', err)