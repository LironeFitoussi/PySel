import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(1)

# ------------------------------------- Alerts -------------------------------------
# Fill the name field
name_text = "Lirone"
name = driver.find_element(By.ID, "name")
name.send_keys(name_text)

# Click on the alert button
alert_button = driver.find_element(By.ID, "alertbtn")
alert_button.click()

# Switch to the alert
alert = driver.switch_to.alert

# Get the text of the alert
alert_text = alert.text
print(alert_text)

# Check the name is inside the alert
assert name_text in alert_text, "Test Name is not in the alert"

# Accept the alert
alert.accept()
# Also can use alert.dismiss() to dismiss the alert in cases the alert is type of confirmation and not just an alert

# Wait 2 seconds
time.sleep(2)