import pytest
from BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editProfile(self, dataLoad):
        logger = self.getLogger()
        logger.info(dataLoad[0])
        logger.info(dataLoad[1])