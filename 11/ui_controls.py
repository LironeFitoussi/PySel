import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(1)

# Checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))
assert len(checkboxes) == 3, "There should be 3 checkboxes"

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected(), "Checkbox is not selected"
        break



# --------------------------------------- Radio Buttons ---------------------------------------
# Radio buttons
radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")

# Print the number of radio buttons
print(len(radio_buttons))

# Click the 2nd radio button
radio_buttons[1].click()

# Check if the 2nd radio button is selected
assert radio_buttons[1].is_selected(), "Radio button is not selected"

# Click the 3rd radio button
radio_buttons[2].click()

# Check if the 2nd radio button is not selected
assert not radio_buttons[1].is_selected(), "Radio button is selected"



# --------------------------------------- Displayed ---------------------------------------
# Displayed
displayed_box = driver.find_element(By.ID, "displayed-text")
assert displayed_box.is_displayed(), "The box is not displayed"

# Hide the box
hide_button = driver.find_element(By.ID, "hide-textbox")
hide_button.click()

# Check if the box is hidden
assert not displayed_box.is_displayed(), "The box is displayed"


# Wait 2 seconds
time.sleep(2)