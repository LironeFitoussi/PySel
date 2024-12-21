from selenium.webdriver.common.by import By
from .checkout_page import CheckoutPage

class HomePage():
    def __init__(self, driver):
        self.driver = driver    
    
    # Shop link 
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    
    # Form submission
    name_input = (By.CSS_SELECTOR, "input[name='name']")
    email_input = (By.NAME, "email")
    password_input = (By.ID, "exampleInputPassword1")
    example_check = (By.ID, "exampleCheck1")
    confirm_button = (By.XPATH, "//input[@value='Submit']")
    
    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click() # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
        # After clicking on the shop link, user will be redirected to the shop page
        
    def fill_name(self, name):
        self.driver.find_element(*HomePage.name_input).send_keys(name)
        
    def fill_email(self, email):
        self.driver.find_element(*HomePage.email_input).send_keys(email)
    
    def fill_password(self, password):
        self.driver.find_element(*HomePage.password_input).send_keys(password)
        
    def click_checkbox(self):
        self.driver.find_element(*HomePage.example_check).click()
    
    def choose_gender(self, gender, gender_selector):
        gender_selector.select_by_visible_text(gender)
    
    def register(self):
        self.driver.find_element(*HomePage.confirm_button).click()
        
    def check_success_message(self):
        success_message = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        return success_message