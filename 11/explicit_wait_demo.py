from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Chrome Driver
from selenium.webdriver.chrome.service import Service
# Chrome 
from selenium.webdriver.common.by import By

service_obj = Service("../chromedriver")
driver = webdriver.Chrome(service=service_obj)

# Implicit Wait
driver.implicitly_wait(5)

# Open URL
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
search_box = driver.find_element(By.CSS_SELECTOR, ".search-keyword")
search_box.send_keys("ber")


results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
assert len(results) > 0, "No results found"

# Add Items to Cart
for result in results:
    result.find_element(By.XPATH, "div/button").click()
        
driver.find_element(By.CSS_SELECTOR, "a[class='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Explicit Wait
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))

# Apply Promo Code
promo_code = driver.find_element(By.CSS_SELECTOR, ".promoCode")
promo_code.send_keys("rahulshettyacademy")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
# Await
time.sleep(2)
