import pytest
from utilities.base_class import BaseClass
from page_objects.home_page import HomePage
from data.shop_page_data import ShopPageData

class TestOne(BaseClass):
    def test_e2e(self, get_data):
        log = self.getLogger()
        driver = self.driver
        try:
            # Home Page Operations
            home_page = HomePage(driver)
            log.info(f"Testing on phone: {get_data['phone']}")
            # Checkout Page Operations
            checkout_page = home_page.shop_items() #! This will return the CheckoutPage object
            checkout_page.add_item(get_data["phone"])
            log.info(f"Added {get_data['phone']} to cart")
            confirm_page = checkout_page.check_out_items() #! This will return the ConfirmPage object
            log.info("Navigated to Confirm Page")
            # Confirm Page Operations
            confirm_page.confirm_purchase()
            confirm_page.find_country("ind")
            country = self.select_country("India")
            country.click()
            log.info("Selected country")
            confirm_page.confirm_checkbox()
            confirm_page.purchase()
            log.info("Purchased the phone")
            success_message = confirm_page.wait_for_success_message()

            assert "Success! Thank you!" in success_message
            
            # Refresh the page
            driver.refresh()
        except Exception as e:
            print(e)
            assert False
            
    @pytest.fixture(params=ShopPageData.test_phones_data)
    def get_data(self, request):
        return request.param