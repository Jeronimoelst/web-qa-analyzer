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

        enlace = driver .find_element(By.LINK_TEXT, "Dropdown")
        enlace.click()

        dropdown = driver.find_element(By.ID, "dropdown")
        opciones = dropdown.find_elements(By.TAG_NAME, "option")
        print(f"Número de opciones encontradas: {len(opciones)}")

        if len(opciones) < 2:
            print("No hay suficientes opciones en el menú desplegable.")
            return
        opcion_seleccionada = opciones[1]
        opcion_seleccionada.click()
        print(f"Opción seleccionada: {opcion_seleccionada.text}")

        assert opcion_seleccionada.is_selected(), \
            f"Error: la opción '{opcion_seleccionada.text}' no está seleccionada."
    finally:
        teardown(driver)