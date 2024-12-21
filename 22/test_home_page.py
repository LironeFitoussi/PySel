import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from utilities.base_class import BaseClass
from page_objects.home_page import HomePage

# Test Data Import
from data.home_page_data import HomePageData


class TestHomePage(BaseClass):
    def test_form_submission(self, get_data):
        log = self.getLogger()
        driver = self.driver
        try:
            log.info(f"Testing on {get_data['first_name']} {get_data['last_name']}")    
            home_page = HomePage(driver)
            home_page.fill_name(get_data["first_name"])
            log.info(f"Filled in first name: {get_data['first_name']}")
            home_page.fill_email(get_data["last_name"])
            log.info(f"Filled in last name: {get_data['last_name']}")
            home_page.fill_password(get_data["password"])
            log.info(f"Filled in password: {get_data['password']}")
            home_page.click_checkbox()
            log.info("Clicked checkbox")
            gender_selector = self.gender_select()
            home_page.choose_gender(get_data["gender"], gender_selector)
            log.info(f"Selected {get_data['gender']} ")
            home_page.register()
            success_message = home_page.check_success_message()
            assert "Success!" in success_message
        except Exception as e:
            print(e)
            assert False
        finally:
            driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("Test Case 1"))
    def get_data(self, request):
        return request.param