from src.logger import set_info_logger, set_error_logger

log_info = set_info_logger()
log_error = set_error_logger()


def get_card_mask(card: str) -> str:
    """
    Возвращает маску карты
    :param card: номер карты на входе
    :return: маска карты в формате xxxx xx** **** xxxx
    """
    log_info.info("Работа функции по получению маски карты.")
    symbols = []

    if len(card) != 16 or not card.isdigit():
        return log_error.error("Неверно указан номер карты!")

    for symbol in range(0, len(card), 4):
        symbols.append(card[symbol: symbol + 4])
    return f"{symbols[0]} {symbols[1][:2]}** **** {symbols[3]}"


def get_bank_account(bank_acc: str) -> str:
    """
    Возвращает маску банковского счета
    :param bank_acc: номер счета на входе
    :return: маска счета в видео ****xx
    """
    log_info.info("Работа функции по получению маски счета.")
    if not bank_acc.isdigit():
        return log_error.error("Неверно указан счет!")

    return f"**{bank_acc[-4:]}"
