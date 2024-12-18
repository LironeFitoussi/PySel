import logging
import inspect

class BaseClass:
    def get_logger(self):
        # Capture the caller's method name for dynamic logging
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # Set the log level
        logger.setLevel(logging.DEBUG)

        # Define log file handler and format
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(file_handler)
        return logger
