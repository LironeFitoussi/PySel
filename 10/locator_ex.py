import time
from selenium import webdriver  # Import the webdriver class
from selenium.webdriver.common.by import By  # Import the By class

driver = webdriver.Chrome()  # Initialize the Chrome driver
driver.get("https://rahulshettyacademy.com/client/")

# Locating Forgot Password link using its CSS Class "forgot-password-link"
forgot_pswd_element = driver.find_element(By.LINK_TEXT, "Forgot password?")
forgot_pswd_element.click()

# Locating Email field
email_field_element = driver.find_element(By.XPATH, "//input[@type='email']")
email_field_element.send_keys("demo@gmail.com")

# Locating Password field
password_field_element = driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input")
password_field_element.send_keys("123456789")

# Locating Confirm Password field
confirm_password_field_element = driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input")
confirm_password_field_element.send_keys("123456789")

# Locating Submit button
submit_button = driver.find_element(By.XPATH, "//button[text()='Save New Password']")
submit_button.click()

time.sleep(5)
