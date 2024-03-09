from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import login
from agregar_usuario import agregar_usuario

@pytest.mark.parametrize("username,password, email, newUsername, newPassword", [
    ("admin@gmail.com", "password", "usuario3@gmail.com", "usuario3", "password"),
])
def test_agregar_usuario(username, password, email, newUsername, newPassword):
    driver = webdriver.Chrome()
    try:
        login(driver,username, password)
        # Esperando que la pagina cargue
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div[2]/div/div/div')))
        assert "You're logged in!" in driver.page_source
        agregar_usuario(driver, newUsername, newPassword, email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div')))
        assert "User created successfully!" in driver.page_source
    finally:
        driver.quit()

