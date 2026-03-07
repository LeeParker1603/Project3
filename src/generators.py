from collections.abc import Generator
from typing import Dict, List


def filter_by_currency(
    transactions: List[Dict], currency_code: str
) -> Generator:
    """
    Функция принимает на вход список словарей, представляющих транзакции,
    и возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)
    """
    if not transactions:
        raise ValueError("Необходимо ввести данные")

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator:
    """
    Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди
    """
    if not transactions:
        raise ValueError("Необходимо ввести данные")

    for transaction in transactions:
        description = transaction["description"]
        yield description


def card_number_generator(start: int, stop: int) -> Generator:
    """
    Генератор, который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    if int(start) > 0 and int(stop) <= 9999999999999999:
        for number in range(int(start), int(stop) + 1):
            card_number = str(number).zfill(16)  # заполняем нулями до 16 цифр
            formatted_card_number = (
                f"{card_number[:4]} {card_number[4:8]} "
                f"{card_number[8:12]} {card_number[12:]}"
            )
            yield formatted_card_number
