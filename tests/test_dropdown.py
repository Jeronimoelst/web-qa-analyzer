'''
Acceda a /dropdown.



Seleccione Option 2.



Compruebe que la opción seleccionada es correcta.



Cierre el navegador correctamente.
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from analizador_web import setup, contar_enlaces, teardown

def test_dropdown():
    driver = setup()

    try:
        assert contar_enlaces(driver) > 0

    driver.find_element(By.LINK_TEXT, "Dropdown").click()
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_value("2")

    assert dropdown.first_selected_option.text == "Option 2"
