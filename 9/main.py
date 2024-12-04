import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Web Driver Check out the local version of the chrome driver, e.g you have the Version 90.0.4430.24 then,
# it downloads the 90.0.4430.24 version of the chrome driver.
# it translates the version of the chrome driver to the version of the chrome browser.
# it downloads the chrome driver from the official site.
# and executes the code.

driver = webdriver.Chrome()
driver.get("https://www.google.com")


# If we want to use a specific version of the chrome driver,
# then we can download the chrome driver from the official site and set the path of the chrome driver to the webdriver.Chrome() method.
service_obj = Service("./chromedriver")
custom_driver = webdriver.Chrome(service=service_obj)
custom_driver.get("https://www.facebook.com")













time.sleep(2)