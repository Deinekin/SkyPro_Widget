from typing import Generator


def filter_by_currency(input_data: list[dict], currency: str) -> filter:
    """
    Принимает список словарей и возвращает итератор, который выдает по очереди операции,
    в которых указана заданная валюта
    :param input_data: список словарей с банковскими данными
    :param currency: валюта, по которой производится фильтрация
    :return: отфильтрованный итератор
    """
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, input_data)


def transaction_descriptions(input_data: list[dict]) -> Generator:
    """
    Принимает список словарей и возвращает описание каждой операции
    :param input_data: список словарей с банковскими данными
    :return: генератор, выдающий описание банковской операции
    """
    return (operation["description"] for operation in input_data)


def card_number_generator(start: int, end: int) -> Generator:
    """
    Генератор номеров карт
    :param start: начальный диапазон номеров карт
    :param end: конечный диапазон номеров карт
    :return: генератор с номерами карт, предстваленными в виде строки
    """
    start_number: str = "0000000000000000"
    for i in range(start, end + 1):
        new_card_number: str = start_number[0:-len(str(i))] + str(i)
        yield ' '.join([new_card_number[0:4], new_card_number[4:8], new_card_number[8:12], new_card_number[12:16]])
