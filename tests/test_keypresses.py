import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from analizador_web import contar_enlaces


@pytest.mark.parametrize(
    ("keypress", "expected"),
    [
        ("A", "A"),
        ("B", "B"),
        (Keys.ENTER, "ENTER"),
    ],
)
def test_key_presses(driver, keypress, expected):
    assert driver.title == "The Internet"
    assert contar_enlaces(driver) > 0

    driver.find_element(By.LINK_TEXT, "Key Presses").click()
    driver.find_element(By.TAG_NAME, "input").send_keys(keypress)

    result = WebDriverWait(driver, 10).until(
        lambda browser: browser.find_element(By.ID, "result").text
        or False
    )
    assert result == f"You entered: {expected}"


def test_enter_submits_form(driver):
    assert driver.title == "The Internet"
    driver.find_element(By.LINK_TEXT, "Key Presses").click()
    url_before_submit = driver.current_url

    driver.find_element(By.TAG_NAME, "input").send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url != url_before_submit
    )
    assert driver.current_url.startswith(url_before_submit)
