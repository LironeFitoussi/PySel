import logging

class BaseClass: 
    def getLogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formatter)
        
        logger.addHandler(fileHandler)
        
        logger.setLevel(logging.CRITICAL)
        return logger