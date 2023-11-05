import pytest

from src.widget import get_card_type_and_mask, get_date


@pytest.mark.parametrize('card, expected', [('Visa Platinum 1111111111111111', 'Visa Platinum 1111 11** **** 1111'),
                                            ('Счет 11111111111111111111', 'Счет **1111'),
                                            ('MasterCard 9999999999999999', 'MasterCard 9999 99** **** 9999'),
                                            ])
def test_get_card_type_and_mask(card, expected):
    assert get_card_type_and_mask(card) == expected


@pytest.mark.parametrize('date, expected', [("2019-06-12T01:26:14.671407", '12.06.2019'),
                                            ("2023-11-05T02:26:18.671407", '05.11.2023'),
                                            ("2018-07-11T02:26:18.671407", '11.07.2018'),
                                            ])
def test_get_date(date, expected):
    assert get_date(date) == expected
