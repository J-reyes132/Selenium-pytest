from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def agregar_usuario(driver, username, password, email):
    driver = driver


    webdriver.ActionChains(driver).click(driver.find_element(By.XPATH, "/html/body/div/main/div/div[1]/nav/a")).perform()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/nav/a[7]")))
    webdriver.ActionChains(driver).click(driver.find_element(By.XPATH, "/html/body/div/div/nav/a[7]")).perform()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div/div[1]/a")))
    webdriver.ActionChains(driver).click(driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/div[1]/a")).perform()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name")))
    username_field = driver.find_element(By.ID,"name")
    password_field = driver.find_element(By.ID,"password")
    email_field = driver.find_element(By.ID,"email")

    username_field.send_keys(username)
    password_field.send_keys(password)
    email_field.send_keys(email)

    password_field.send_keys(Keys.ENTER)
    