# Child Window
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service_obj = Service("../chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

# Click on page link at //a[contains(text(),'Free Access to')]
driver.find_element(By.XPATH, "//a[contains(text(),'Free Access to')]").click()

# print(driver.window_handles)
# Switch to Child Window
child_window = driver.window_handles[1]
driver.switch_to.window(child_window)

# Get Text From //p[@class='im-para red']
text_element = driver.find_element(By.XPATH, "//p[@class='im-para red']")

# Extrand the text of innet Strong Tag
text = text_element.find_element(By.TAG_NAME, "strong").text

driver.close()
driver.switch_to.window(driver.window_handles[0])

# send the text to the input field  //input[@id='username']
driver.find_element(By.ID, "username").send_keys(text)

# Send Password to the input field //input[@id='password']
driver.find_element(By.ID, "password").send_keys("password")

# Click on Sign in Button  //input[@id='signInBtn']
driver.find_element(By.ID, "signInBtn").click()

# 5 secodns for //div[@class='alert alert-danger col-md-12']
wait = WebDriverWait(driver, 10)
wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[@class='alert alert-danger col-md-12']")
    )
)

print("Alert Element Found")

# Locate the element
alert_element = driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']")
WebDriverWait(driver, 10).until(lambda driver: alert_element.text != "")
# Get the full text of the element
alert_text = alert_element.text


print(f"Alert Text: {alert_text}")
# Assert the text content
assert alert_text == "Incorrect username/password.", "Alert text does not match!"

print("Test Passed")
time.sleep(10)
