import pandas as pd
from typing import Any
from pprint import pprint


def set_dict(row_of_file: list) -> Any:
    """
    Заполняет словарь элементами списка, состоящего из данных о транзакции
    :param row_of_file: строка из .csv или .xlsx файла с данными о транзакции
    :param file:
    :return: словарь, значениями которого являются элементы поданного на вход списка
    """
    return {
        "id": row_of_file[0],
        "state": row_of_file[1],
        "date": str(row_of_file[2])[:-1],
        "operationAmount": {"amount": row_of_file[3],
                            "currency": {"currency_name": row_of_file[4],
                                         "currency_code": row_of_file[5]}},
        "from": row_of_file[6],
        "to": row_of_file[7],
        "description": row_of_file[8],
    }


def read_csv_or_xlsx_file(file: str) -> list[dict]:
    """
    Считываем .csv или .xlsx файл, данные грузим в словарь, создаем из словарей список
    :param file: путь до .csv или .xlsx файла
    :return: список словарей с данными о транзакциях
    """
    list_of_transactions_from_file: list = []
    if file.endswith('.csv'):
        df = pd.read_csv(file, delimiter=';', encoding='utf-8', dtype=str)
        for row in df.iterrows():
            list_of_transactions_from_file.append(set_dict(row[1].to_list()))
    if file.endswith('.xlsx'):
        df = pd.read_excel(file, dtype=str)
        for row in df.iterrows():
            list_of_transactions_from_file.append(set_dict(row[1].to_list()))

    return list_of_transactions_from_file
