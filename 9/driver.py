import time
from selenium import webdriver

# If we want to use another browser, then we can use the following code.
# driver = webdriver.Firefox()
# driver = webdriver.Edge()
# driver = webdriver.Safari()
# driver = webdriver.Ie()

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Expanding the window
driver.maximize_window()

# Getting the title of the page
print(driver.title) 

# Getting the current URL of the page
print(driver.current_url)

















time.sleep(2)