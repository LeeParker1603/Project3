from typing import Any, List

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


# Тест, что функция корректно фильтрует транзакции
# по заданной валюте
def test_filter_by_currency(
    transactions_list: List, transactions_result: List
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
def test_transaction_descriptions():
    pass


# Тестируем работу функции с различным количеством
# входных транзакций, включая пустой список
def test_transaction_descriptions_empty():
    pass


# Тест, который проверяет, что генератор выдает
# правильные номера карт в заданном диапазоне
def test_card_number_generator():
    pass


# Проверяем корректность форматирования номеров карт
def test_card_number_generator_format():
    pass


# Проверяем, что генератор корректно обрабатывает крайние
# значения диапазона и правильно завершает генерацию
def test_card_number_generator_correct():
    pass
