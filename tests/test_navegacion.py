
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from analizador_web import setup, title, contar_enlaces, teardown




def test_links():
    driver = setup()
    try:
        contador_enlaces = contar_enlaces(driver)

        if contador_enlaces == 0:
            return {
                "estado": "FAIL",
                "url": driver.current_url,
                "descripcion": "No se encontraron enlaces en la página"
            }

        assert driver.title == "The Internet"

        return {
            "estado": "PASS",
            "url": driver.current_url,
            "descripcion": f"Se encontraron {contador_enlaces} enlaces y el título es correcto"
        }

    except AssertionError:
        return {
            "estado": "FAIL",
            "url": driver.current_url,
            "descripcion": "El título de la página no coincide"
        }

    except Exception as e:
        return {
            "estado": "ERROR",
            "url": driver.current_url,
            "descripcion": str(e)
        }

    finally:
        teardown(driver)
