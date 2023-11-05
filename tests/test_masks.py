import pytest

from src.masks import get_card_mask, get_bank_account


@pytest.mark.parametrize("card, expected", [('1234567890123456', '1234 56** **** 3456'),
                                            ('1111111111111111', '1111 11** **** 1111'),
                                            ('2222222222222222', '2222 22** **** 2222'),
                                            ])
def test_get_card_mask(card, expected):
    assert get_card_mask(card) == expected


def test_get_card_mask_invalid_card():
    assert get_card_mask('a111111111111111') == "Неверно указана карта"
    assert get_card_mask('1234') == "Неверно указана карта"


@pytest.mark.parametrize("bank_acc, expected", [('12345678901234560000', '**0000'),
                                                ('11111111111111111111', '**1111'),
                                                ('22222222222222222222', '**2222'),
                                                ])
def test_get_bank_account(bank_acc, expected):
    assert get_bank_account(bank_acc) == expected


def test_get_bank_account_invalid_acc():
    assert get_bank_account('b123123124b1231231') == "Неверно указан счет"
