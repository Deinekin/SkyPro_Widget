import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def bank_data():
    transactions = (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]
    )
    return transactions


def test_filter_by_currency(bank_data):
    usd_transactions = filter_by_currency(bank_data, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268


def test_filter_by_currency_out_of_data(bank_data):
    usd_transactions = filter_by_currency(bank_data, "USD")
    with pytest.raises(StopIteration):
        assert next(usd_transactions)["id"] == 939719570
        assert next(usd_transactions)["id"] == 142264268
        assert next(usd_transactions)["id"] == 895315941
        assert next(usd_transactions)["id"] == 895315941


def test_transaction_descriptions(bank_data):
    descriptions = transaction_descriptions(bank_data)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"


def test_transaction_descriptions_out_of_data(bank_data):
    descriptions = transaction_descriptions(bank_data)
    with pytest.raises(StopIteration):
        assert next(descriptions) == "Перевод организации"
        assert next(descriptions) == "Перевод со счета на счет"
        assert next(descriptions) == "Перевод со счета на счет"
        assert next(descriptions) == "Перевод с карты на карту"
        assert next(descriptions) == "Перевод организации"
        assert next(descriptions) == "Перевод организации"


@pytest.mark.parametrize('start, end, expected', [(1, 5, ["0000 0000 0000 0001",
                                                          "0000 0000 0000 0002",
                                                          "0000 0000 0000 0003",
                                                          "0000 0000 0000 0004",
                                                          "0000 0000 0000 0005"]),
                                                  (10, 15, ["0000 0000 0000 0010",
                                                            "0000 0000 0000 0011",
                                                            "0000 0000 0000 0012",
                                                            "0000 0000 0000 0013",
                                                            "0000 0000 0000 0014",
                                                            "0000 0000 0000 0015"]),
                                                  ])
def test_card_number_generator(start, end, expected):
    for _ in range(start, end + 1):
        assert next(card_number_generator(start, end + 1)) == next(iter(expected))
