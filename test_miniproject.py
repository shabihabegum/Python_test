from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver_path = r"C:\Users\shabi\OneDrive\Desktop\Python_test\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# form details fill up
driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")
driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
driver.find_element(By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]/label").click()
driver.find_element(By.ID, "userNumber").send_keys("9876543210")

# Select date of birth
dob_input = driver.find_element(By.ID, "dateOfBirthInput")
dob_input.click()
dob_input.send_keys(Keys.CONTROL + "a")  # Select all text
dob_input.send_keys("01 Jan 2000")       # Format: DD MMM YYYY
dob_input.send_keys(Keys.ENTER)  

# Select subjects
subjects = ["Maths", "English"]

subject_input = driver.find_element(By.ID, "subjectsInput")

for subject in subjects:
    subject_input.send_keys(subject)
    time.sleep(1)  # Wait for dropdown to appear
    subject_input.send_keys(Keys.ENTER)


# Select hobbies
hobbies = ["Sports", "Reading"]

for hobby in hobbies:
    driver.find_element(By.XPATH, f"//label[contains(text(), '{hobby}')]").click()

# Upload picture
file_path = r"C:\Users\shabi\OneDrive\Desktop\Python_test\test.png"

# Confirm file exists before sending
if os.path.exists(file_path):
    upload = driver.find_element(By.ID, "uploadPicture")
    upload.send_keys(file_path)
else:
    print("❌ File does not exist. Please check the path.")

# Fill address
driver.find_element(By.ID, "currentAddress").send_keys("123 Automation Lane, Test City")

# select state
state = driver.find_element(By.XPATH, "//*[@id='react-select-3-input']")
state.send_keys("NCR")
state.send_keys(Keys.ENTER)
time.sleep(2)

# select city
city = driver.find_element(By.XPATH, "//*[@id='react-select-4-input']")
city.send_keys("Delhi")
city.send_keys(Keys.ENTER)
time.sleep(2)

# submit
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
time.sleep(2)
# submit_button.click()
# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
# print("Form is submitted successfully")

try:
    submit_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
    print("Form is submitted successfully")
except Exception as e:
    print(f"❌ Form submission failed: {e}")

driver.quit()
