from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


# Тестирование фильтрации списка словарей по заданному статусу
# state
@pytest.mark.parametrize(
    "user_data_list, output_list",
    zip(
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
)
def test_filter_by_state_correct(
    user_data_list: List[Dict], output_list: List[Dict]
) -> None:
    assert user_data_list == output_list


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
