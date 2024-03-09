from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def agregar_producto(driver, name, price, quantity, description, categories):
    driver = driver
    file_path = '/home/jreyes/personal/Calidad-software/tarea-9/OculusScreenshot1689308267.jpeg'
    webdriver.ActionChains(driver).click(driver.find_element(By.XPATH, "/html/body/div/main/div/div[1]/nav/a")).perform()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/nav/a[2]")))
    webdriver.ActionChains(driver).click(driver.find_element(By.XPATH, "/html/body/div/div/nav/a[2]")).perform()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div/div[1]/a")))
    webdriver.ActionChains(driver).click(driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/div[1]/a")).perform()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name")))
    name_field = driver.find_element(By.ID,"name")
    price_field = driver.find_element(By.ID,"price")
    stock_field = driver.find_element(By.ID,"quantity")
    description_field = driver.find_element(By.ID,"body")
    image_field = driver.find_element(By.ID,"image")
    category_field = driver.find_element(By.ID,"categories")

    name_field.send_keys(name)
    price_field.send_keys(price)
    stock_field.send_keys(quantity)
    description_field.send_keys(description)
    category_field.send_keys(categories)
    image_field.send_keys(file_path)


    stock_field.send_keys(Keys.ENTER)