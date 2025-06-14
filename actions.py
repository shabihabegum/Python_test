from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
import time

driver_path = r"C:\Users\shabi\OneDrive\Desktop\Python_test\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/slider")
driver.maximize_window()



# range selection
# actions = ActionChains(driver)
# slider = driver.find_element(By.ID, "sliderContainer")
# actions.click_and_hold(slider).move_by_offset(-slider.size['width'] // 2, 0).release().perform()
# time.sleep(2)
# actions.click_and_hold(slider).move_by_offset(51, 0).release().perform()
# # driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));", slider, "51")

# value = driver.find_element(By.ID, "sliderValue").get_attribute("value")
# print(value)
# print("success #2")


slider = driver.find_element(By.CLASS_NAME, "range-slider")
slider_width = slider.size['width']
target_value = 51
# Convert the desired value to a pixel offset (approximate)
offset = int((target_value / 100) * slider_width) - (slider_width // 2)

actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(offset, 0).release().perform()

value = driver.find_element(By.ID, "sliderValue").get_attribute("value")
print(value)
print("success #2")