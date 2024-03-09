from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import login
from agregar_producto import agregar_producto

@pytest.mark.parametrize("username,password, name, price, quantity, description, categories", [
    ("admin@gmail.com", "password", "producto de prueba", "100", "2", "descripcion de prueba", "categoria de prueba"),
])
def test_agregar_producto(username, password, name, price, quantity, description, categories):
    driver = webdriver.Chrome()
    try:
        login(driver,username, password)
        # Esperando que la pagina cargue
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div[2]/div/div/div')))
        assert "You're logged in!" in driver.page_source
        agregar_producto(driver, name, price, quantity, description, categories)
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div')))
        # assert "Menu created successfully!" in driver.page_source
    finally:
        driver.quit()

