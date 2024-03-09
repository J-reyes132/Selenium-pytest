from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

def borrar_usuario(driver, usernameDelete):
    driver = driver
    webdriver.ActionChains(driver).click(driver.find_element(By.XPATH, "/html/body/div/main/div/div[1]/nav/a")).perform()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/nav/a[7]")))
    webdriver.ActionChains(driver).click(driver.find_element(By.XPATH, "/html/body/div/div/nav/a[7]")).perform()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[6]/div/form/button")))
    webdriver.ActionChains(driver).click(driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[6]/div/form/button")).perform()

    alert = driver.switch_to.alert

    alert.accept()