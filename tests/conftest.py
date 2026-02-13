from typing import Any, Dict, List

import pytest


# Фикстура пустого значения
@pytest.fixture
def empty() -> str:
    return ""


# Фикстура подстановки значений через лист
@pytest.fixture(
    params=["5465464", "0", "58882425499887787878789988798", "368"]
)
def list_numbers_non_conform(request: Any) -> Any:
    return request.param


# Фикстура для предоставления тестовых данных список словарей,
# включая одинаковые даты.
@pytest.fixture
def operations() -> List[Dict]:
    return [
        {"id": 1, "date": "2022-03-01T12:30:00.000000"},
        {"id": 2, "date": "2022-01-15T08:45:00.000000"},
        {"id": 3, "date": "2022-03-01T12:30:00.000000"},  # одинаковая дата
        {"id": 4, "date": "2022-02-20T09:15:00.000000"},
    ]


# Фикстура для предоставления тестовых данных список словарей
# где отсутствует state по умолчанию
@pytest.fixture
def state_non_default() -> List[Dict]:
    return [
        {
            "id": 41428829,
            "state": "dssdfff",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "CANCELED",
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
    ]


# Фикстура для предоставления тестовых данных список словарей,
# c некорректными датами.
@pytest.fixture
def non_correct_date() -> List[Dict]:
    return [
        {"id": 1, "date": "20225-03-01T12:30:00.000000"},
        {"id": 2, "date": "2022-31-15T08:45:00.000000"},
        {"id": 3, "date": "00022-03-01T12:30:00.000000"},
        {"id": 4, "date": "2022-02-2200T09:15:00.000000"},
    ]
