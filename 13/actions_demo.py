# Actions Class
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time
service_obj = Service("../chromedriver")
options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Actions Class
action = ActionChains(driver)

#? double_click => Double Click
# double_click = driver.find_element(By.ID, "mousehover")

#? context_click => Right Click
# context_click = driver.find_element(By.ID, "mousehover")

#? drag_and_drop => Drag and Drop
# drag = driver.find_element(By.ID, "source")

# Perform Action of Hovering over an Element 
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

time.sleep(6)