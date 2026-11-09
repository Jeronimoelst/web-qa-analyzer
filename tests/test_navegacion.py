from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from analizador_web import setup, title, contar_enlaces, teardown



def test_links():
    driver = setup()

    
    try:
            title(driver)
    
            cantidad = contar_enlaces(driver)
    
            assert len(cantidad) > 0, "No se encontraron enlaces en la página"
    
            print(f"PASS: Se encontraron {len(cantidad)} enlaces")
    
    finally:
            teardown(driver)

test_links()



