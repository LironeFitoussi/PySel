from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service_obj = Service("/Users/lironefitoussi/Developer/PySel/chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("--headless")


options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
options.add_argument("window-size=1400,800")

driver = webdriver.Chrome(service=service_obj, options=options)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# //a[contains(href,'shop')] - Xpath for shop button
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

# Phaze 1 - Find the product and add it to the cart
for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

# Phaze 2 - Go to the cart
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

# Phaze 3 - Checkout
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()

# Phaze 4 - Enter the country
driver.find_element(By.ID, "country").send_keys("ind")

# 4a - Wait for the country to appear
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

# 4b - Click the checkbox
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

# 4c - Click the purchase button
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

# Phaze 5 - Get the success message

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
success_message = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in success_message

driver.close()
print("Test Passed")
# time.sleep(10)

