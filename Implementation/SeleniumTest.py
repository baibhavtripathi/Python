from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import win32com.client as win32
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("http://localhost:8080/camunda/app/cockpit/default/#/login")
try:
    # Wait for up to 5 seconds for the element to be present
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
    )
    print("Element is ready!")
    username_input = driver.find_element(By.XPATH, "//input[@type='text']")
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")

    username_input.send_keys("demo")  # Replace with your username
    password_input.send_keys("demo")  # Replace with your password
    password_input.send_keys(Keys.RETURN)  # Press Enter to submit the form

    # Wait for login to process
    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.NAME, '//a[contains(@href, "#/processes")]'))
    # )
    # Navigate to the "Processes" section or a specific process page
    # Assuming the "Processes" tab is visible after login
    driver.get('http://localhost:8080/camunda/app/cockpit/default/#/processes')
    time.sleep(5)

except:
    print("Element not found within 5 seconds.")
finally: 
    # Close the browser
    driver.quit()
'''
username_input = driver.find_element(By.XPATH, "//input[@type='text']")
password_input = driver.find_element(By.XPATH, "//input[@type='password']")

username_input.send_keys("demo")  # Replace with your username
password_input.send_keys("demo")  # Replace with your password
password_input.send_keys(Keys.RETURN)  # Press Enter to submit the form

# Wait for login to process
time.sleep(5000)

# Navigate to the "Processes" section or a specific process page
# Assuming the "Processes" tab is visible after login

# processes_tab = driver.find_element(By.XPATH, '//a[contains(@href, "/camunda/app/cockpit/default/#/process-instance/")]')
# processes_tab.click()

# Wait for the process page to load
time.sleep(3)

driver.quit()
'''