from typing import List, Any


def filter_by_currency(transactions: List, currency_code: str) -> List:
    """
    Функция принимает на вход список словарей, представляющих транзакции,
    и возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)
    """
    if not transactions:
        raise ValueError("Необходимо ввести данные")

    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction



def transaction_descriptions():
    pass



def card_number_generator():
    pass