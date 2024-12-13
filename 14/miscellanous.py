from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
service_obj = Service("../chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--ignore-certificate-errors") # Ignore SSL errors
# Set the window size
options.add_argument("window-size=1400,800")

driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# ```JavaScript
#   window.scrollTo(0, document.body.scrollHeight); // Scroll to the bottom of the page
# ```

# Execute JavaScript to scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Take a Screenshot
driver.get_screenshot_as_file("screenshot.png")

# time.sleep(6)