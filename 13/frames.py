from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service_obj = Service("../chromedriver")
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://the-internet.herokuapp.com/iframe")

# Implicit Wait
driver.implicitly_wait(5)

# Switch to Frame
driver.switch_to.frame("mce_0_ifr")

# Wait for the editable area to load
editable_area = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "tinymce"))
)

# Check if the element is editable
is_editable = driver.execute_script(
    "return arguments[0].getAttribute('contenteditable');", editable_area
)

if is_editable == "false":
    # Make it editable using JavaScript
    driver.execute_script("arguments[0].setAttribute('contenteditable', 'true');", editable_area)

# Clear the existing text and input new text
editable_area.clear()
editable_area.send_keys("I am able to automate")

# Switch back to the main content
driver.switch_to.default_content()

# Add a small delay to observe the result (optional)
time.sleep(5)

# Quit the browser
driver.quit()