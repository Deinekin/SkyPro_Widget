import os

from src.pandas_utils import read_csv_or_xlsx_file

transaction_dict = ({'id': '650703',
                     'state': 'EXECUTED',
                     'date': '2023-09-05T11:30:32',
                     'operationAmount': {'amount': '16210',
                                         'currency': {'currency_code': 'PEN',
                                                      'currency_name': 'Sol'}},
                     'from': 'Счет 58803664561298323391',
                     'to': 'Счет 39745660563456619397',
                     'description': 'Перевод организации'})


def test_read_csv_or_xlsx_file():
    assert read_csv_or_xlsx_file(os.path.abspath('data/transactions_excel.xlsx'))[0] == transaction_dict
    assert read_csv_or_xlsx_file(os.path.abspath('data/transactions.csv'))[0] == transaction_dict
