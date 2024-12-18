import logging
# import pytest

# Initialize the logger
logger = logging.getLogger(__name__)

# Set the level of the logger
logger.setLevel(logging.INFO)  # Logs INFO, WARNING, ERROR, and CRITICAL

# Format the logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

# Create a formatter and set the format for the logs - This will format the logs
file_handler = logging.FileHandler("logfile.log")

# Set the level of the logs
file_handler.setFormatter(formatter)

# Create a file handler - This handler will write the logs to a file
logger.addHandler(file_handler)


#? Define the log level - DEBUG, INFO, WARNING, ERROR, CRITICAL

# Debug - Detailed information, typically of interest only when diagnosing problems.
logger.debug('This is a debug message')

# Info - Confirmation that things are working as expected.
logger.info('This is an info message')

# Warning - An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
logger.warning('This is a warning message')

# Error - Due to a more serious problem, the software has not been able to perform some function.
logger.error('This is an error message')

# Critical - A serious error, indicating that the program itself may be unable to continue running.
logger.critical('This is a critical message')


def test_logging_demo():
    logger.info("Starting test_logging_demo.")
    logger.warning("Simulated warning in the test case.")
    logger.error("Simulated error in the test case.")
    logger.critical("Simulated critical issue in the test case.")

logger.setLevel(logging.DEBUG)
logger.info("This will not appear.")
logger.error("This will appear.")