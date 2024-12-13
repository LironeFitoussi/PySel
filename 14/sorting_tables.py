from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service("/Users/lironefitoussi/Developer/PySel/chromedriver")
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
# Set the window size
options.add_argument("window-size=1400,800")

driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browserSortedVeggieList = []
# Click on the column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# Collect all the veggie names -> BrowserSortedVeggieList (A, B, C, D) | In Case of Bug -> (A, B, D, C)
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")  # A, B, C, D
for element in veggieWebElements:
    # print(element.text)
    browserSortedVeggieList.append(element.text)

OriginaVeggielList = browserSortedVeggieList.copy()

# Sort this BrowserSortedVeggieList => NewSortedVeggieList
browserSortedVeggieList.sort()

# Assert NewSortedVeggieList == BrowserSortedVeggieList
assert OriginaVeggielList == browserSortedVeggieList, "The list is not sorted"

print("The list is sorted")