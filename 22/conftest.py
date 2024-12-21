import pytest
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from datetime import datetime

# Command Line Options:
def pytest_addoption(parser):
    # Browser Options
    parser.addoption("--browser_name", action="store", default="chrome")
    
    # Environment Options
    parser.addoption("--run-env", action="store", default="dev") # dev, qa, prod

@pytest.fixture(scope="class")
def setup(request):
    # Set up the WebDriver
    global driver
    url = None
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        service = Service("../chromedriver")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "safari":
        options = webdriver.SafariOptions()
        options.add_argument("--headless")
        driver = webdriver.Safari(options=options)
    
    # Set the URL based on the environment
    env = request.config.getoption("--run-env")
    if env == "dev":
        url = "https://rahulshettyacademy.com/angularpractice/"
    elif env == "qa":
        url = "https://rahulshettyacademy.com/angularpractice/"
    elif env == "prod":
        url = "https://rahulshettyacademy.com/angularpractice/"
    
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshots in HTML report, whenever a test fails.
    :param item: The test item.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Generate a unique screenshot name
            file_name = report.nodeid.replace("::", "_") + ".png"
            screenshot_path = _capture_screenshot(file_name)
            if screenshot_path:
                html = (
                    '<div>'
                    f'<img src="/{screenshot_path}" alt="screenshot" '
                    'style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/>'
                    '</div>'
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    """
    Captures a screenshot and saves it in the reports/screenshots directory.
    :param name: The screenshot file name.
    :return: The relative path to the screenshot.
    """
    try:
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{current_time}_{name}")
        
        # Ensure `driver` is properly initialized before this function is called
        driver.get_screenshot_as_file(screenshot_path)
        return screenshot_path
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return None