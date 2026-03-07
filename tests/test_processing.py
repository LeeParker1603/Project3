from typing import Any, Dict, List

import pytest

from src.processing import (filter_by_state, process_bank_operations,
                            process_bank_search, sort_by_date)


# Тестирование фильтрации списка словарей по заданному статусу
# state
@pytest.mark.parametrize(
    "user_data_list, output_list",
    [
        (
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
            ],
        ),
        (
            [
                {
                    "id": 41428829,
                    "state": "CANCELED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "EXECUTED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "EXECUTED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "EXECUTED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "EXECUTED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
        ),
    ],
)
def test_filter_by_state_correct(
    user_data_list: List[Dict], output_list: List[Dict]
) -> None:
    assert filter_by_state(user_data_list) == output_list


# Проверка работы функции при отсутствии словарей с указанным статусом
# state в списке, а также при различных возможных вариантах state.
def test_filter_by_state_non_default(
    state_non_default: List[Dict],
) -> None:
    assert filter_by_state(state_non_default) == []


# Тестирование сортировки списка словарей по датам
# в порядке убывания и возрастания, и с совпадающими датами
@pytest.mark.parametrize(
    "reverse_order, expected_ids",
    [
        (True, [1, 3, 4, 2]),  # Убывающий порядок
        (False, [2, 4, 1, 3]),  # Возрастающий порядок
    ],
)
def test_sort_by_date_order(
    operations: List[Dict], reverse_order: bool, expected_ids: List
) -> None:
    sorted_operations = sort_by_date(operations, reverse_order)
    result_ids = [op["id"] for op in sorted_operations]
    assert result_ids == expected_ids


# Тестирование сортировки списка словарей по датам
# в порядке убывания и возрастания, с некорректными датами.
@pytest.mark.parametrize(
    "reverse_order, expected_ids",
    [
        (True, [1, 2, 4, 3]),  # Убывающий порядок
        (False, [3, 4, 2, 1]),  # Возрастающий порядок
    ],
)
def test_sort_by_date_non_correct(
    non_correct_date: List[Dict], reverse_order: bool, expected_ids: List
) -> None:
    sorted_operations = sort_by_date(non_correct_date, reverse_order)
    result_ids = [op["id"] for op in sorted_operations]
    assert result_ids == expected_ids


def test_process_bank_search_success() -> None:
    """Тест успешного поиска по подстроке (регистронезависимо)"""
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "перевод с карты"},
    ]
    # Должен найти и "Перевод", и "перевод"
    result = process_bank_search(data, "перевод")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод организации"
    assert result[1]["description"] == "перевод с карты"


def test_process_bank_search_no_results() -> None:
    """Тест ситуации, когда совпадений нет"""
    data = [{"description": "Оплата услуг"}]
    result = process_bank_search(data, "Кредит")
    assert result == []


def test_process_bank_search_with_non_string_data() -> None:
    """Тест обработки некорректных данных (например, NaN/float из Excel)"""
    data: list[dict[str, Any]] = [
        {"description": "Перевод"},
        {"description": None},  # Имитация пустой ячейки
        {"description": 12345},  # Имитация числа
    ]
    # Проверяем, что функция не падает (благодаря str() в коде)
    result = process_bank_search(data, "Перевод")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод"


def test_process_bank_search_empty_data() -> None:
    """Тест на пустом списке данных"""
    assert process_bank_search([], "test") == []


def test_process_bank_search_special_chars() -> None:
    """Тест поиска строки со спецсимволами (благодаря re.escape)"""
    data = [{"description": "Перевод (карта) + бонус"}]
    # Символы ()+ не должны сломать регулярное выражение
    result = process_bank_search(data, "(карта) +")
    assert len(result) == 1


def test_process_bank_operations_basic() -> None:
    """Тест базового подсчета категорий"""
    data = [
        {"description": "Перевод организации"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Оплата услуг"},
    ]
    categories = ["Перевод организации", "Открытие вклада", "Кредит"]

    result = process_bank_operations(data, categories)

    # Проверяем количество
    assert result["Перевод организации"] == 2
    assert result["Открытие вклада"] == 1
    # Категория, которой не было в данных, должна быть 0
    assert result["Кредит"] == 0


def test_process_bank_operations_empty_data() -> None:
    """Тест с пустым списком операций"""
    categories = ["Перевод", "Вклад"]
    result = process_bank_operations([], categories)

    # Все категории должны вернуться со значением 0
    assert result == {"Перевод": 0, "Вклад": 0}


def test_process_bank_operations_no_categories() -> None:
    """Тест с пустым списком искомых категорий"""
    data = [{"description": "Перевод"}]
    result = process_bank_operations(data, [])
    assert result == {}


def test_process_bank_operations_missing_description() -> None:
    """Тест обработки словарей без ключа 'description'"""
    data: list[dict[str, Any]] = [
        {"description": "Перевод"},
        {"amount": 100},  # Ключа description нет
        {},  # Пустой словарь
    ]
    categories = ["Перевод"]

    # Функция не должна упасть (благодаря .get())
    result = process_bank_operations(data, categories)
    assert result["Перевод"] == 1


def test_process_bank_operations_case_sensitivity() -> None:
    """
    Тест на чувствительность к регистру
    (по умолчанию 'Перевод' != 'перевод')
    """
    data = [{"description": "ПЕРЕВОД"}]
    categories = ["перевод"]
    result = process_bank_operations(data, categories)

    # Так как в коде нет .lower(), совпадения не будет
    assert result["перевод"] == 0
