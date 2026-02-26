from typing import Any, Dict, List

import pytest


# Фикстура пустого значения
@pytest.fixture
def empty() -> Any:
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


# Фикстура для предоставления тестовых данных список словарей,
# Для проверки функций filter_by_currency и
# transaction_descriptions
@pytest.fixture
def transactions_list() -> List[Dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


# Фикстура для значений, которые возвращает
# функция filter_by_currency
@pytest.fixture
def transactions_result() -> List[Dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


# Фикстура для тестирования рубля
@pytest.fixture
def rub_transaction() -> Any:
    return {"operationAmount": {"amount": 100.50, "currency": {"code": "RUB"}}}


# Фикстура для доллара
@pytest.fixture
def usd_transaction() -> Any:
    return {"operationAmount": {"amount": 10, "currency": {"code": "USD"}}}
