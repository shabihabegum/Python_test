from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = r"C:\Users\shabi\OneDrive\Desktop\Python_test\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://seleniumbase.io/demo_page")
driver.find_element(By.ID, "myTextInput").send_keys("Selenium Test")
driver.find_element(By.ID, "myButton").click()
text = driver.find_element(By.ID, "readOnlyText").get_attribute("value")
print(text)
time.sleep(5)


# iFrame
iframe1 = driver.find_element(By.ID, "myFrame1")
driver.switch_to.frame(iframe1)
image = driver.find_element(By.TAG_NAME, "img")
img_src = image.get_attribute("src")
print (img_src)


driver.quit()