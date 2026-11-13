'''

Tu objetivo es automatizar el siguiente proceso:
1. Inicializar el navegador con setup().
2. Acceder a la página.
3. Localizar el botón Start.
4. Pulsar el botón.
5. Implementar una espera explícita para detectar el texto que aparece después de la carga.
6. Capturar una posible TimeoutException.
7. Registrar el error utilizando logging.
8. Comprobar mediante assert que aparece el texto Hello World!.
9. Cerrar el navegador con teardown().
Nuevos conceptos que debes aplicar:
- WebDriverWait
- expected_conditions
- TimeoutException
- logging.exception()
- assert
- try / except / finally
'''
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

from analizador_web import setup, contar_enlaces, teardown

logging.basicConfig(level=logging.INFO)

def test_esperas():
    driver = setup()

    contador_enlaces = contar_enlaces(driver)
    if contador_enlaces == 0:
        logging.error("No se encontraron enlaces en la página.")
        teardown()
        return
    try:
        dinamic_loading_url = driver.find_element(driver, By.LINK_TEXT, "Dynamic Loading")
        dinamic_loading_url.click()

        example_1_url = driver.find_element(driver, By.LINK_TEXT, "Example 1: Element on page that is hidden")
        example_1_url.click()

        start_button = driver.find_element(driver, By.CSS_SELECTOR, "#start button")
        start_button.click()

        try:
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
            )
        except TimeoutException:
            logging.exception("TimeoutException: El texto 'Hello World!' no apareció en el tiempo esperado.")
            raise
    finally:
        teardown()