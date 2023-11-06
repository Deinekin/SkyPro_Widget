def get_card_mask(card: str) -> str:
    """
    Возвращает маску карты
    :param card: номер карты на входе
    :return: маска карты в формате xxxx xx** **** xxxx
    """
    symbols = []

    if len(card) != 16 or not card.isdigit():
        return "Неверно указана карта"

    for symbol in range(0, len(card), 4):
        symbols.append(card[symbol: symbol + 4])
    return f"{symbols[0]} {symbols[1][:2]}** **** {symbols[3]}"


def get_bank_account(bank_acc: str) -> str:
    """
    Возвращает маску банковского счета
    :param bank_acc: номер счета на входе
    :return: маска счета в видео ****xx
    """
    if not bank_acc.isdigit():
        return "Неверно указан счет"

    return f"**{bank_acc[-4:]}"
