from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 


def setup():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    return driver



def title(driver):
    heading = driver.find_element(By.TAG_NAME, "h1")
    print(f"Título de la página: {heading.text}")
    titulo = heading.text
    wait = WebDriverWait(driver, 10)
    assert titulo == "Welcome to the-internet"
    

def contar_enlaces(driver):
    enlaces = driver.find_elements(By.TAG_NAME, "a")
    wait = WebDriverWait(driver, 10)
    print(f"Enlaces encontrados: {len(enlaces)}")
    return len(enlaces)
    

def teardown(driver):
    driver.quit()


