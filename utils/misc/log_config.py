import logging
from data import config
from loguru import logger


f = "{time:YYYY-MM-DD H:m:ss} | {level} | {message} | {name}:{function}:{line}"
f_e = "{time:YYYY-MM-DD H:m:ss}\nLevel: {level}\nMessage: {message}\nLine: {name}:{function}:{line}"


def setup():
    logger.add(config.LOGS_BASE_PATH + "/errors.log",
               filter=lambda record: record['level'].no == logging.ERROR,
               format=f_e,
               rotation="10 KB",
               compression="tar.gz")
    logger.add(config.LOGS_BASE_PATH + "/info.log",
               filter=lambda record: record['level'].no == logging.INFO,
               format=f,
               rotation="512 KB",
               compression="tar.gz")
    logger.add(config.LOGS_BASE_PATH + "/debug.log",
               filter=lambda record: record['level'].no == logging.DEBUG,
               format=f,
               rotation="10 KB",
               compression="tar.gz")
