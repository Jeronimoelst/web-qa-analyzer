from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from analizador_web import contar_enlaces, setup, teardown

def test_dropdown(driver):
    
    driver = setup()
    assert contar_enlaces(driver) > 0
    try:
        assert driver.title == "The Internet"
        
        dropdown_element = driver.find_element(By.LINK_TEXT, "Dropdown")
        dropdown_element.click()

        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        if dropdown.select_by_value("2") is None:
            return {
                "estado": "FAIL",
                "url": driver.current_url,
                "descripcion": "No se pudo seleccionar la opción 2 del dropdown"
            }
        else:
            return {
                "estado": "PASS",
                "url": driver.current_url,
                "descripcion": "Se seleccionó correctamente la opción 2 del dropdown"
            }       
  
    except Exception as e:
        return {
            "estado": "ERROR",
            "url": driver.current_url,
            "descripcion": str(e)
        }
    finally:
        teardown(driver)