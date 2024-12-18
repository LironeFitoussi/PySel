from base_class import BaseClass

class TestEditProfile(BaseClass):
    def test_logging_demo(self):
        logger = self.get_logger()
        logger.info("Test case started")
        logger.debug("Loading test data...")
        logger.error("An error occurred!")  # Example log level usage
