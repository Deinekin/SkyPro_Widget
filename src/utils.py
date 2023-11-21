import json
from src.logger import set_info_logger, set_error_logger

log_info = set_info_logger()
log_error = set_error_logger()


def get_json(path: str) -> list[dict]:
    """
    Принимаем на вход путь до JSON-файла и возвращаем список словарей с данными о финансовых транзакциях
    :param path: строковый путь до JSON-файла, если файл не найден или ошибка декодирования - возвращаем пустой список
    :return: список словарей
    """
    log_info.info("Начало работы функции по получению списка словарей из .json файла")
    try:
        with open(path, 'r', encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Ошибка при преобразовании в JSON данных из файла")
                log_error.error("Ошибка при преобразовании в JSON данных из файла")
                return []
    except FileNotFoundError:
        print("Не найден файл")
        log_error.error("Не найден файл")
        return []


def get_sum_of_transaction(transaction: dict) -> float:
    """
    Функция для получения суммы транзакции, если она была совершена в рублях
    :param transaction: словарь с данными о транзакции
    :return: сумма в рублях или ошибка
    """
    log_info.info("Начало работы функции по получению суммы транзакции")
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        log_error.error("Операция указана не в рублях")
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
