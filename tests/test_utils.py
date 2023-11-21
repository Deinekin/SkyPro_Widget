import pytest
import os
from src.utils import get_json, get_sum_of_transaction


@pytest.fixture
def dict_rub():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


@pytest.fixture
def dict_usd():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }


def test_get_json():
    assert get_json(os.path.abspath('data/test_valid.json')) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]
    assert get_json(os.path.abspath('data/test_invalid.json')) == []
    assert get_json(os.path.abspath('data/operations1.json')) == []


def test_get_json_decode_error():
    assert get_json(os.path.abspath('data/test_invalid.json')) == []


def test_get_json_file_not_found_error():
    assert get_json(os.path.abspath('data/operations1.json')) == []


def test_get_sum_of_transaction_rub(dict_rub):
    assert get_sum_of_transaction(dict_rub) == 31957.58


def test_get_sum_of_transaction_invalid(dict_usd):
    with pytest.raises(ValueError):
        get_sum_of_transaction(dict_usd)
