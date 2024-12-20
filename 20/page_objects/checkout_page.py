from selenium.webdriver.common.by import By
from .confirm_page import ConfirmPage
from selenium.common.exceptions import NoSuchElementException
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    product_card = (By.XPATH, "//div[@class='card h-100']")
    card_footer = (By.XPATH, "//button[@class='btn btn-info']")
    check_out = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    
    def get_product_cards(self):
        return self.driver.find_elements(*CheckoutPage.product_card)
    
    def add_item(self, product_name):
        # Retrieve the list of product cards on the webpage
        products = self.get_product_cards()
        
        # Flag to check if the product is found and added
        product_added = False

        # Iterate through each product card
        for product in products:
            try:
                # Extract the product name text from the product card
                product_name_text = product.find_element(By.XPATH, "div/h4/a").text
                
                # Check if the product name matches the provided name
                if product_name_text == product_name:
                    # Click the "Add to Cart" button
                    product.find_element(By.XPATH, "div/button").click()
                    product_added = True
                    print(f"Product '{product_name}' added to cart successfully.")
                    break
            except NoSuchElementException:
                # Handle cases where expected elements are not found in the product card
                print(f"Warning: Missing expected elements in a product card. Skipping...")

        # Assert that the product was added successfully
        assert product_added, f"Error: Product '{product_name}' was not found or could not be added to the cart."
                

            
    def check_out_items(self):
        self.driver.find_element(*CheckoutPage.check_out).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page # after clicking on the checkout button, user will be redirected to the confirm page
    