import logging
from loguru import logger
from data import config


def setup():
    logger.add(config.LOGS_BASE_PATH + "/errors.log", filter=lambda record: record['level'] == logging.ERROR)
    logger.add(config.LOGS_BASE_PATH + "/info.log", filter=lambda record: record['level'] == logging.INFO)
    logger.add(config.LOGS_BASE_PATH + "/debug.log", filter=lambda record: record['level'] == logging.DEBUG)
