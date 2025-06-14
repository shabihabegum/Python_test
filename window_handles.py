from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = r"C:\Users\shabi\OneDrive\Desktop\Python_test\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()

main_window = driver.current_window_handle

# open new tab
new_tab = driver.find_element(By.ID, "tabButton").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
assert "This is a sample page" in driver.page_source, "Tab is not found"
print("tab success")
time.sleep(2)
driver.close()

driver.switch_to.window(main_window)
time.sleep(2)



# open new window

driver.find_element(By.ID, "windowButton").click()
driver.switch_to.window(driver.window_handles[1])
assert "This is a sample page" in driver.page_source, "Window is not found"
print("window success")
time.sleep(2)
driver.close()

driver.switch_to.window(main_window)
time.sleep(2)



# switch to message window

driver.find_element(By.ID, "messageWindowButton").click()
new_window = driver.switch_to.window(driver.window_handles[1])
print("message window success")
time.sleep(2)
driver.close()
# message = driver.execute_script("return document.body ? document.body.textContent : ''")

# if message:
#     print("✅ Message in New Window Message:", message.strip())
# else:
#     print("❌ Message content not found.")

driver.switch_to.window(main_window)
time.sleep(2)