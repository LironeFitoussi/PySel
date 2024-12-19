import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="class")
def setup(request):
    # Set up the WebDriver
    service = webdriver.chrome.service.Service('C:/Users/USER/Downloads/chromedriver_win32/chromedriver.exe')
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()