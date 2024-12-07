import time
from selenium import webdriver  # Import the webdriver class
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.support.ui import Select  # Import the Select class

# Hide Window
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Setup Chrome driver
driver = webdriver.Chrome(
    # options=options
)

# Open a webpage
driver.get("https://rahulshettyacademy.com/angularpractice/")

# locating name_element - CSS Selector
# CSS Selector: tagname[attribute='value']: e.g. input[type='submit']
# Using ID: tagname#id: e.g. input#exampleInputPassword1
# Using Class: tagname.classname: e.g. input.form-control
name_element = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
name_element.send_keys("Lirone")

# locating email_element
email_element = driver.find_element(By.NAME, "email")
email_element.send_keys("lirone@gmail.com")

# locating password_element
password_element = driver.find_element(By.ID, "exampleInputPassword1")
password_element.send_keys("123456")

# locating checkbox_element
checkbox_element = driver.find_element(By.ID, "exampleCheck1")
checkbox_element.click()

# locating Select Dropdown
# Xpath: //tagname[@attribute='value'] or //tagname[@id='value']
# CSS Selector: tagname[attribute='value']: e.g. select#exampleFormControlSelect1
select_dropdown = Select(
    driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1")
)
select_dropdown.select_by_visible_text("Female")  # Select by visible text
select_dropdown.select_by_index(1)  # Deselect by index
# select_dropdown.select_by_value("Mmale") # Select by value attribute

# locating Submit button
# Xpath: //tagname[@attribute='value'] or //tagname[@id='value']
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()

# Locate the success message
success_message = driver.find_element(By.CLASS_NAME, "alert-success")

# Locate the employee status multi-select checkbox
employee_status = driver.find_element(By.CSS_SELECTOR, "#inlineRadio1")
employee_status.click()

# Locate "Two way data binding" text box using Xpath as 3rd element
two_way_data_binding = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
two_way_data_binding.send_keys("Lirone")
two_way_data_binding.clear()


# Check if the success message is displayed
assert success_message.is_displayed(), "Success message is not displayed"

# Check if the success message text is correct
assert "Success" in success_message.text, "Success message text is incorrect"

# # Wait for 3 seconds NOT USING WEBDRIVER WAIT
time.sleep(3)

# Close the browser
driver.quit()


# Print Success message of QA Test Automation
print("QA Test Automation is successful")

# End of the script
