import pandas as pd
from typing import Any


def set_dict(row_of_file: list, file: str) -> Any:
    """
    Заполняет словарь элементами списка, состоящего из данных о транзакции
    :param row_of_file: строка из .csv или .xlsx файла с данными о транзакции
    :param file:
    :return: словарь, значениями которого являются элементы поданного на вход списка
    """
    transaction_dict = {
        "id": None,
        "state": row_of_file[1],
        "date": str(row_of_file[2])[:-1],
        "operationAmount": {"amount": None,
                            "currency": {"currency_name": row_of_file[4],
                                         "currency_code": row_of_file[5]}},
        "from": row_of_file[6],
        "to": row_of_file[7],
        "description": row_of_file[8],
    }
    if file.endswith('.csv'):
        transaction_dict["id"] = row_of_file[0]
        transaction_dict["operationAmount"]["amount"] = row_of_file[3]
    else:
        transaction_dict["id"] = str(row_of_file[0])[:-2]
        transaction_dict["operationAmount"]["amount"] = str(row_of_file[3])[:-2]
    return transaction_dict


def read_csv_or_xlsx_file(file: str) -> list[dict]:
    """
    Считываем .csv или .xlsx файл, данные грузим в словарь, создаем из словарей список
    :param file: путь до .csv или .xlsx файла
    :return: список словарей с данными о транзакциях
    """
    list_of_transactions_from_file: list = []
    if file.endswith('.csv'):
        df = pd.read_csv(file, delimiter=';', encoding='utf-8')
        for row in df.iterrows():
            list_of_transactions_from_file.append(set_dict(row[1].to_list(), file))
    if file.endswith('.xlsx'):
        df = pd.read_excel(file)
        for row in df.iterrows():
            list_of_transactions_from_file.append(set_dict(row[1].to_list(), file))

    return list_of_transactions_from_file
