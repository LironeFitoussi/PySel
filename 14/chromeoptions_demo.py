from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service("/Users/lironefitoussi/Developer/PySel/chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("--headless")


options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
options.add_argument("window-size=1400,800")

driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

print(driver.title)