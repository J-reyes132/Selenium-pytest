from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import login
from borrar_usuario import borrar_usuario


@pytest.mark.parametrize("username,password, usernameDelete", [
    ("admin@gmail.com", "password", "usuario3"),
])

def test_borrar_usuario(username, password, usernameDelete):
    driver = webdriver.Chrome()
    try:
        login(driver,username, password)
        # Esperando que la pagina cargue
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div[2]/div/div/div')))
        assert "You're logged in!" in driver.page_source
        borrar_usuario(driver, usernameDelete)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div/span')))
        assert "User deleted successfully!" in driver.page_source
    finally:
        driver.quit()