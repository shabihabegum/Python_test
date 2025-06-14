from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = r"C:\Users\shabi\OneDrive\Desktop\Python_test\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/frames")
driver.maximize_window()

iframe = driver.find_element(By.ID, "frame1")
driver.switch_to.frame(iframe)
iframe_text = driver.find_element(By.TAG_NAME, "body").text
assert "This is a sample page" in iframe_text, "Frame is not found"
print("success")

driver.switch_to.default_content()
print(driver.title)

driver.quit()