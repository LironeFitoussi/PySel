import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_class import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        driver = self.driver
        try:
            driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
            products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

            # Phaze 1 - Find the product and add it to the cart
            for product in products:
                product_name = product.find_element(By.XPATH, "div/h4/a").text
                if product_name == "Blackberry":
                    product.find_element(By.XPATH, "div/button").click()

            # Phaze 2 - Go to the cart
            driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

            # Phaze 3 - Checkout
            driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()

            # Phaze 4 - Enter the country
            driver.find_element(By.ID, "country").send_keys("ind")

            # 4a - Wait for the country to appear
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
            driver.find_element(By.LINK_TEXT, "India").click()

            # 4b - Click the checkbox
            driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

            # 4c - Click the purchase button
            driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

            # Phaze 5 - Get the success message

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
            success_message = driver.find_element(By.CLASS_NAME, "alert-success").text

            assert "Success! Thank you!" in success_message
        except:
            print("An error occurred")
            assert False
        finally:
            time.sleep(5)
            driver.quit()