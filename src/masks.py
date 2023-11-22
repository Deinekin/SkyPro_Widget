from src.logger import setup_logging
from typing import Any
logger = setup_logging()


def get_card_mask(card: str) -> str | Any:
    """
    Возвращает маску карты
    :param card: номер карты на входе
    :return: маска карты в формате xxxx xx** **** xxxx
    """
    logger.info("Работа функции по получению маски карты.")
    symbols = []

    if len(card) != 16 or not card.isdigit():
        logger.error("Неверно указан номер карты!")
        return logger.info("Завершена работа функции по получению маски карты.")

    for symbol in range(0, len(card), 4):
        symbols.append(card[symbol: symbol + 4])

    logger.info("Завершена работа функции по получению маски карты.")
    return f"{symbols[0]} {symbols[1][:2]}** **** {symbols[3]}"


def get_bank_account(bank_acc: str) -> str | Any:
    """
    Возвращает маску банковского счета
    :param bank_acc: номер счета на входе
    :return: маска счета в видео ****xx
    """
    logger.info("Работа функции по получению маски счета.")
    if not bank_acc.isdigit():
        logger.info("Завершена работа функции по получению маски счета.")
        return logger.error("Неверно указан счет!")

    logger.info("Завершена работа функции по получению маски счета.")
    return f"**{bank_acc[-4:]}"
