'''
Acceda a /checkboxes.



Compruebe cuántas casillas existen.



Marque las casillas que estén desmarcadas.
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from analizador_web import setup, contar_enlaces, teardown

def test_check_boxes():
    driver = setup()

    try:
        assert contar_enlaces(driver) > 0

        enlace = driver.find_element(By.LINK_TEXT, "Checkboxes")
        enlace.click()

        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        print(f"Número de casillas encontradas: {len(checkboxes)}")

        if len(checkboxes) == 0:
            print("No se encontraron casillas de verificación.")
            return

        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
                print("Casilla marcada.")
            else:
                print("Casilla ya estaba marcada.")
        assert all(checkbox.is_selected() for checkbox in checkboxes), \
    "Error: no todas las casillas están marcadas."
    finally:
        teardown(driver)
        