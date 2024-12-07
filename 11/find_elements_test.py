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
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

dropdown_element = driver.find_element(By.CSS_SELECTOR , "#autosuggest")
dropdown_element.send_keys("ind")

time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

# print the number of options
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# print(driver.find_element(By.ID, "autosuggest").text) #! This will not work
# print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

# Assertion
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India", "Country is not India"
time.sleep(2)
