
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def login(driver, username, password):
    driver = driver
    driver.get("http://127.0.0.1:8000")

    webdriver.ActionChains(driver).click(driver.find_element(By.XPATH, "/html/body/div[1]/nav/div[2]/a[2]")).perform()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    
    username_field = driver.find_element(By.ID,"email")
    password_field = driver.find_element(By.ID,"password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    password_field.send_keys(Keys.ENTER)
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div[2]/div/div/div')))

