from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from analizador_web import setup, title, contar_enlaces, teardown





def test_textbox_ab():
    try:
        driver = setup()
        assert contar_enlaces(driver) > 0

        text_box = driver.find_element(By.ID, "example-filter")
        text_box.click()
        text_box.send_keys("A/B Testing")
        assert text_box.get_attribute("value") == "A/B Testing"
       


        enlace = driver.find_element(By.LINK_TEXT, "A/B Testing")
        enlace.click()

        titulo = driver.title
        print(f"Título de la página: {titulo}")

        assert titulo in ["A/B Test Control", "A/B Test Variation 1"], (
            f"El título de la página no es el esperado. "
            f"Se esperaba 'A/B Test Control' o 'A/B Test Variation 1', "
            f"pero se obtuvo '{titulo}'"
        )
    except Exception as e:
        print(f"Error al realizar la prueba: {e}")

    finally:
        teardown(driver)
