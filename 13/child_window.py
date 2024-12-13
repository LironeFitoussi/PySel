# Child Window
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service("../chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://the-internet.herokuapp.com/windows")

# Find Element
driver.find_element(By.LINK_TEXT, "Click Here").click()

# print(driver.window_handles)
# Switch to Child Window
child_window = driver.window_handles[1]
driver.switch_to.window(child_window)
# print(driver.find_element(By.TAG_NAME, "h3").text)
assert driver.find_element(By.TAG_NAME, "h3").text == "New Window", "Child Window is not correct"

driver.close()
driver.switch_to.window(driver.window_handles[0])

assert "Opening a new window" in driver.find_element(By.TAG_NAME, "h3").text, "Parent Window is not correct"

print("Test Passed")