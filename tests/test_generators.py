from typing import Any, Dict, List

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


# Тест, что функция корректно фильтрует транзакции
# по заданной валюте
def test_filter_by_currency(
    transactions_list: List[Dict], transactions_result: List
) -> None:
    usd_transactions = list(filter_by_currency(transactions_list, "USD"))
    assert len(usd_transactions) > 0  # Убедились, что есть транзакции в USD
    assert all(
        transactions["operationAmount"]["currency"]["code"] == "USD"
        for transactions in usd_transactions
    )
    assert usd_transactions == transactions_result


# Тест, что функция не завершается ошибкой при обработке
# пустого списка
# или списка без соответствующих валютных операций
def test_filter_by_currency_empty(empty: Any) -> None:
    currency_empty = filter_by_currency(empty, empty)
    with pytest.raises(ValueError, match="Необходимо ввести данные"):
        # Преобразуем в список, чтобы запустить генератор
        list(currency_empty)


# Тест, что функция возвращает корректные описания
# для каждой транзакции
@pytest.mark.parametrize(
    "descriptions_res",
    [
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]
    ],
)
def test_transaction_descriptions(
    transactions_list: List[Dict], descriptions_res: List
) -> None:
    assert (
        list(transaction_descriptions(transactions_list)) == descriptions_res
    )


# Тестируем работу функции transaction_descriptions
# на пустой список
def test_transaction_descriptions_empty(empty: Any) -> None:
    currency_empty = transaction_descriptions(empty)
    with pytest.raises(ValueError, match="Необходимо ввести данные"):
        # Преобразуем в список, чтобы запустить генератор
        list(currency_empty)


# Тест, который проверяет, что генератор выдает
# правильные номера карт в заданном диапазоне.
# Проверяем корректность форматирования номеров карт
# Проверяем, что генератор корректно обрабатывает крайние
# значения диапазона и правильно завершает генерацию
@pytest.mark.parametrize(
    "start, stop, gen_numbers",
    [
        (
            5,
            7,
            [
                "0000 0000 0000 0005",
                "0000 0000 0000 0006",
                "0000 0000 0000 0007",
            ],
        ),
        (
            55788,
            55793,
            [
                "0000 0000 0005 5788",
                "0000 0000 0005 5789",
                "0000 0000 0005 5790",
                "0000 0000 0005 5791",
                "0000 0000 0005 5792",
                "0000 0000 0005 5793",
            ],
        ),
        (
            88888888888,
            88888888894,
            [
                "0000 0888 8888 8888",
                "0000 0888 8888 8889",
                "0000 0888 8888 8890",
                "0000 0888 8888 8891",
                "0000 0888 8888 8892",
                "0000 0888 8888 8893",
                "0000 0888 8888 8894",
            ],
        ),
        (0, 15, []),  # проверяем крайнее значение start
        (
            9999999999999999999,
            9999999999999999999999999999999,
            [],
        ),  # проверяем крайнее значение stop
        (
            "1",
            "3",
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),  # проверяем преобразование из строки в int
    ],
)
def test_card_number_generator(
    start: int, stop: int, gen_numbers: List
) -> None:
    assert list(card_number_generator(start, stop)) == gen_numbers
