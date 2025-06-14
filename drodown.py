from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains 
import time

driver_path = r"C:\Users\shabi\OneDrive\Desktop\Python_test\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()


# dropdown selection
dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))
dropdown.select_by_visible_text("Purple")
time.sleep(2)
print("success #1")
driver.close()

