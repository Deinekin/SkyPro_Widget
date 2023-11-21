import logging
from typing import Any


def set_info_logger() -> Any:
    """
    Функция для логирования информации
    :return: лог информации
    """
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler('data_file.log', encoding='utf-8')
    file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger


def set_error_logger() -> Any:
    """
    Функция для логирования ошибок
    :return: лог ошибки
    """
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler('data_file.log', encoding='utf-8')
    file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.ERROR)
    return logger
