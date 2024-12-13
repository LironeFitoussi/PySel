from selenium import webdriver
import time
# Chrome Driver
from selenium.webdriver.chrome.service import Service
# Chrome 
from selenium.webdriver.common.by import By

service_obj = Service("../chromedriver")
driver = webdriver.Chrome(service=service_obj)

# Implicit Wait
driver.implicitly_wait(5)
# 5 Seconds Implicit Wait, if element is found in 2 seconds, it will go to next step immediately ans save 3 seconds
# If element is not found in 5 seconds, it will throw an error

# Open URL
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
search_box = driver.find_element(By.CSS_SELECTOR, ".search-keyword")
search_box.send_keys("ber")

# Wait for 2 seconds
# time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
assert len(results) > 0, "No results found"

# Add Items to Cart
for result in results:
    result.find_element(By.XPATH, "div/button").click()
        
driver.find_element(By.CSS_SELECTOR, "a[class='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# time.sleep(2)
# Apply Promo Code
promo_code = driver.find_element(By.CSS_SELECTOR, ".promoCode")
promo_code.send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Await
time.sleep(2)
