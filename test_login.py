from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import login

@pytest.mark.parametrize("username,password", [
    ("admin@gmail.com", "password"),
])
def test_login(username, password):
    driver = webdriver.Chrome()
    try:
        login(driver,username, password)
        # Esperando que la pagina cargue
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div[2]/div/div/div')))
        assert "You're logged in!" in driver.page_source
    finally:
        driver.quit()

