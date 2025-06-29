import logging

def log():
    logging.basicConfig(filename="..\\Logs\\logfile.log", format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    logger = logging.getLogger()
    # log.info("This is first logging")
    return logger

logger = log()
logger.info("This is a new log")
