import re
from collections import Counter


def get_list_by_key(input_list: list[dict], key: str = "EXECUTED") -> list[dict]:
    """
    принимает на вход список словарей и значение для ключа state
    и возвращает новый список, содержащий только те словари, у которых ключ
    state содержит переданное в функцию значение
    :param input_list: список словарей
    :param key: значение для ключа state, по умолчанию == EXECUTED
    :return: список словарей по значению ключа state
    """
    new_list: list[dict] = []
    for element in input_list:
        if element['state'] == key:
            new_list.append(element)
    return new_list


def sort_by_date(input_list: list[dict], by_raise: bool = True) -> list[dict]:
    """
    принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы
    по убыванию даты
    :param input_list: список словарей
    :param by_raise: сортируем по убыванию или по возрастанию, True = по убыванию
    :return: отсортированный по дате список словарей
    """
    return sorted(input_list, key=lambda element: element['date'], reverse=by_raise)


def search_by_description(transactions: list[dict], description: str) -> list[dict]:
    """
    Создает новый список словарей, которые в описании имеют заданную пользователем строку
    :param transactions: список словарей с данными о банковских операциях
    :param description: описание операции, по которой будет производиться поиск
    :return: список словарей, у которых в описании есть заданная строка
    """
    return [transaction for transaction in transactions if
            re.search(description.lower(), transaction['description'].lower())]


def count_operations_by_category(transactions: list[dict], category_operations: dict) -> dict:
    """

    :param transactions: список словарей с данными о банковских операциях
    :param category_operations:
    :return: словарь, где ключи - описание операций, а значения 0 количество таких операций
    """
    return dict(Counter([transaction['description'] for transaction in transactions]))
