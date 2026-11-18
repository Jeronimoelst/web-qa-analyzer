from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from analizador_web import contar_enlaces, setup, teardown


def test_check_boxes():
    driver = setup()

    try:
        assert driver.title == "The Internet"
        contador_enlaces = contar_enlaces(driver)
        
        if contador_enlaces == 0:
                    return {
                        "estado": "FAIL",
                        "url": driver.current_url,
                        "descripcion": "No se encontraron enlaces en la página"
                    }
        
        enlace = driver.find_element(By.LINK_TEXT, "Checkboxes")
        enlace.click()

        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

        if not checkboxes:
             return {
                "estado": "FAIL",
                "url": driver.current_url,
                "descripcion": "No se encontraron casillas de verificación en la página"
             }
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
        if all(checkbox.is_selected() for checkbox in checkboxes):
            return {
                "estado": "PASS",
                "url": driver.current_url,
                "descripcion": f"Se encontraron {len(checkboxes)} casillas de verificación y todas están marcadas"
            }
        return {
            "estado": "FAIL",
            "url": driver.current_url,
            "descripcion": "No todas las casillas de verificación están marcadas"
        }
    except Exception as e:
        return {
            "estado": "ERROR",
            "url": driver.current_url,
            "descripcion": str(e)
        }

    finally:
        teardown(driver)
        