from selenium import webdriver
from selenium.webdriver.common.by import By



def setup():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    return driver



def title(driver):
    titulo = driver.title
    assert titulo == "Welcome to the-internet"
    

def contar_enlaces(driver):
    enlaces = driver.find_elements(By.TAG_NAME, "a")
    print(f"Enlaces encontrados: {len(enlaces)}")
    return len(enlaces)
    

def teardown(driver):
    driver.quit()



driver = setup()
title(driver)
teardown(driver)