from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Chrome Driver
from selenium.webdriver.chrome.service import Service
# Chrome 
from selenium.webdriver.common.by import By

service_obj = Service("../chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(service=service_obj, options=options)

# Implicit Wait
driver.implicitly_wait(5)

# Open URL
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
search_box = driver.find_element(By.CSS_SELECTOR, ".search-keyword")
search_box.send_keys("ber")

# Sleep for 2 seconds
time.sleep(2)
execpeted_results_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
recived_results_list = []

assert len(results) > 0, "No results found"

# Add Items to Cart
for result in results:
    recived_results_list.append(result.find_element(By.XPATH, ".//h4").text)
    result.find_element(By.XPATH, ".//div[@class='product-action']/button").click()

assert len(execpeted_results_list) == len(recived_results_list), "Results are not the same"

#? for result in recived_results_list:
#?     assert result in execpeted_results_list, f"Product {result} is not in the expected results list"    

assert execpeted_results_list == recived_results_list, "Results are not the same"

driver.find_element(By.CSS_SELECTOR, "a[class='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Values of Items
items = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
total_price = 0
for price in items:
    total_price += int(price.text)

# Find Total Price
total = driver.find_element(By.XPATH, "//span[@class='totAmt']")
assert total.text == str(total_price), "Total Price is not correct"

print(f"Total Price: {total.text}")
# Explicit Wait
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))

# Apply Promo Code
promo_code = driver.find_element(By.CSS_SELECTOR, ".promoCode")
promo_code.send_keys("rahulshettyacademy")

# Click Apply
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10) 
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

# Find Discounted Percentage
discounted_percentage = driver.find_element(By.XPATH, "//span[@class='discountPerc']").text
# Cut the % sign eg. 10%
discounted_percentage = discounted_percentage[:-1]

# Find Discounted Price
discounted_price = driver.find_element(By.XPATH, "//span[@class='discountAmt']").text
discounted_price = float(discounted_price)

# Check if the discounted price is less than the total price
assert discounted_price < total_price, "Discounted Price is not less than Total Price"
assert discounted_price == total_price - total_price * (float(discounted_percentage) / 100), "Discounted Price is not correct"

print(f"Discounted Price: {discounted_price}")

# Await
time.sleep(2)
