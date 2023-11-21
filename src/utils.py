import json


def get_json(path: str) -> list[dict]:
    """
    Принимаем на вход путь до JSON-файла и возвращаем список словарей с данными о финансовых транзакциях
    :param path: строковый путь до JSON-файла, если файл не найден или ошибка декодирования - возвращаем пустой список
    :return: список словарей
    """
    try:
        with open(path, 'r', encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Ошибка при преобразовании в JSON данных из файла")
                return []
    except FileNotFoundError:
        print("Не найден файл")
        return []


def get_sum_of_transaction(transaction: dict) -> float:
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
