# Any Pytest file should start with test_ or end with _test
# Pytest method names should start with test
# Any code should be wrapped in method only
# To run tests, go to terminal and type pytest -v -s
# -v is for verbose, -s is for console output
# We can mark the test cases using the decorator @pytest.mark
import pytest
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

@pytest.mark.smoke
@pytest.mark.skip
def test_first_program():
    print("Hello World")
    assert driver.title == "ProtoCommerce", "Title is not matching" # This will pass

def test_second_program_alpha():
    print("Hello World 2")
    assert driver.title == "ProtoCommerce - ProtoCommerce", "Title is not matching" # This will fail
    
# used Flag -s to see the print statements in the console
# used Flag -v to see the verbose output of the test cases