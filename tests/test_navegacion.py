from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from analizador_web import setup, title, contar_enlaces, teardown


driver = setup()
title(driver)
contar_enlaces(driver)


def test_links():
    driver = setup()

    
    try:
            title(driver)
    
            cantidad = contar_enlaces(driver)
    
            assert len(cantidad) > 0, "No se encontraron enlaces en la página"
    
            print(f"PASS: Se encontraron {len(cantidad)} enlaces")
    
    finally:
            teardown(driver)


def test_key_presses(keypresses):
    driver = setup()

    try:
        assert contar_enlaces(driver) > 0

        enlace = driver.find_element(By.LINK_TEXT, "Key Presses")
        enlace.click()

        campo_entrada = driver.find_element(By.TAG_NAME, "input")
        campo_entrada.send_keys(keypresses)

        resultado = driver.find_element(By.ID, "result").text

        print(f"Resultado obtenido: {resultado}")

        assert resultado == f"You entered: {keypresses}", (
            f"Resultado esperado: 'You entered: {keypresses}', "
            f"pero se obtuvo: '{resultado}'"
        )

    finally:
        teardown(driver)


test_key_presses("A")
test_key_presses("B")
test_key_presses(Keys.ENTER)



