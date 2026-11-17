import pytest
from selenium.webdriver.common.by import By

from analizador_web import contar_enlaces


@pytest.mark.parametrize(
    ("keypresses", "expected"),
    [
        ("A", "A"),
        ("B", "B"),
    ],
)
def test_key_presses(driver, keypresses, expected):
    assert contar_enlaces(driver) > 0

    driver.find_element(By.LINK_TEXT, "Key Presses").click()
    driver.find_element(By.TAG_NAME, "input").send_keys(keypresses)
    resultado = driver.find_element(By.ID, "result").text

    assert resultado == f"You entered: {expected}"
