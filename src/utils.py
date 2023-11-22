import json
from src.logger import setup_logging

logger = setup_logging()


def get_json(path: str) -> list[dict]:
    """
    Принимаем на вход путь до JSON-файла и возвращаем список словарей с данными о финансовых транзакциях
    :param path: строковый путь до JSON-файла, если файл не найден или ошибка декодирования - возвращаем пустой список
    :return: список словарей
    """
    logger.info("Начало работы функции по получению списка словарей из .json файла")
    try:
        with open(path, 'r', encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                logger.error("Завершена работа функции по получению списка словарей."
                             "Ошибка при преобразовании в JSON данных из файла")
                return []
    except FileNotFoundError:
        logger.error("Завершена работа функции по получению списка словарей. Файл не найден")
        return []


def get_sum_of_transaction(transaction: dict) -> float:
    """
    Функция для получения суммы транзакции, если она была совершена в рублях
    :param transaction: словарь с данными о транзакции
    :return: сумма в рублях или ошибка
    """
    logger.info("Начало работы функции по получению суммы транзакции")
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("Завершена работа функции по получению суммы транзакции")
        return float(transaction["operationAmount"]["amount"])
    else:
        logger.error("Завершена работа функции по получению суммы транзакции. Операция указана не в рублях")
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
