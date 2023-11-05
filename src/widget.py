from masks import get_card_mask, get_bank_account


def get_card_type_and_mask(card: str) -> str:
    """
    Возвращает маску карты с типом карты
    :param card: данные карты в виде строки типа "Visa Platinum xxxxxxxxxxxxxxxx"
    :return: данные карты в виде строки типа "Visa Platinum xxxx xx** **** xxxx"
    """
    card_info_list = card.split(" ")
    if "Счет" in card_info_list:
        return f"Счет {get_bank_account(card_info_list[-1])}"
    else:
        card_info_list[-1] = get_card_mask(card_info_list[-1])
        return " ".join(card_info_list)


def get_date(date: str) -> str:
    """
    Возвращает дату в формате dd.mm.yy
    :param date: строка, например "2018-07-11T02:26:18.671407"
    :return: дата, например "11.07.2018"
    """
    date_list = date.split("-")
    return f"{date_list[2][:2]}.{date_list[1]}.{date_list[0]}"
