from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import random

options = Options()
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver_path = r"C:\Users\shabi\OneDrive\Desktop\Python_test\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys("standard_user")

placeholder_value = driver.find_element(By.ID, "user-name").get_attribute("placeholder")
print(placeholder_value) # This will print the placeholder value of the username field

driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# alert = driver.switch_to.alert
# alert.accept()

add_product = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
random_product = random.sample(add_product, 2)

for product in random_product:
    product.click()
    time.sleep(2)

driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(2)



