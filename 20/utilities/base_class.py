import pytest
import inspect
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        if not logger.handlers:  # Check if handlers already exist
            file_handler = logging.FileHandler('logfile.log')
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.setLevel(logging.DEBUG)
        return logger
        
    def select_country(self, country_name):
        contry_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, country_name)))
        return contry_element
    
    def gender_select(self):
        gender_select = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        return gender_select