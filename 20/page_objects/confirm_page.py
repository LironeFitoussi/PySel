from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    confirm_button = (By.XPATH, "//button[@class='btn btn-success']")
    country_input = (By.ID, "country")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit_button = (By.CSS_SELECTOR, "input[type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")
    def confirm_purchase(self):
        self.driver.find_element(*ConfirmPage.confirm_button).click()
        
    def find_country(self, country):
        self.driver.find_element(*ConfirmPage.country_input).send_keys(country)
        
    def select_country(self, country):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, country)))
        self.driver.find_element(By.LINK_TEXT, country).click()
        
    def confirm_checkbox(self):
        self.driver.find_element(*ConfirmPage.checkbox).click()
        
    def purchase(self):
        self.driver.find_element(*ConfirmPage.submit_button).click()
        
    def wait_for_success_message(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ConfirmPage.success_message))
        success_message = self.driver.find_element(*ConfirmPage.success_message).text
        return success_message