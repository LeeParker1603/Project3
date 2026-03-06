import logging
from typing import Any
from unittest.mock import patch

from main import main

# Отключаем логирование ПЕРЕД импортом модулей
logging.disable(logging.CRITICAL)


@patch("main.get_transactions_from_json")
@patch("builtins.input")
@patch("builtins.print")
def test_main_full_run_json(
    mock_print: Any, mock_input: Any, mock_get_json: Any
) -> None:
    """
    Тестируем сценарий JSON-файла и варианты ответа пользователя
    """
    # 1. Мокаем JSON-файл:
    mock_get_json.return_value = [
        {
            "date": "2019-12-08T22:46:21.307722",
            "description": "Открытие вклада",
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "to": "Счет 64686453677032553056",
        },
        {
            "date": "2020-12-08T22:46:21.307722",
            "description": "Перевод",
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {"name": "USD", "code": "USD"},
            },
            "to": "Счет 64686453677032553056",
        },
    ]

    # 2. Имитируем ответы пользователя:
    # 1 (JSON) -> EwXECUTED (Статус неверно) -> EXECUTED (Статус) ->
    # ajs;k (Дата неверно) -> да (Дата) -> да (Сортируем - неверно) ->
    # по убыванию (Сортируем) -> дава (Валюта неверно) -> да (Валюта) ->
    # два (Поиск неверно) -> да (Поиск) -> открытие (ключевое слово)
    mock_input.side_effect = [
        "5",
        "1",
        "EwXECUTED",
        "EXECUTED",
        "ajs;k",
        "да",
        "да",
        "по убыванию",
        "дава",
        "да",
        "два",
        "да",
        "открытие",
    ]

    # 3. Запускаем
    main()

    # 4. Проверяем, что в консоль вывелось количество операций
    # Ищем среди всех вызовов print строку,
    # содержащую "Всего банковских операций"
    printed_texts = [
        call.args[0] for call in mock_print.call_args_list if call.args
    ]
    assert any(
        "Всего банковских операций в выборке: 1" in text
        for text in printed_texts
    )


@patch("main.load_csv")
@patch("builtins.input")
@patch("builtins.print")
def test_main_full_scenario_csv(
    mock_print: Any, mock_input: Any, mock_get_csv: Any
) -> None:
    """
    Тестируем сценарий CSV-файла
    """
    # 1. Мокаем CSV-файл:
    mock_get_csv.return_value = [
        {
            "date": "2019-12-08T22:46:21.307722",
            "description": "Открытие вклада",
            "state": "CANCELED",
            "amount": "41096.24",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "from": "Счет 64686453677032553056",
            "to": "Счет 64686453677032553056",
        }
    ]

    # 2. Имитируем ответы пользователя:
    # 2 (CSV) -> CANCELED (Статус) -> нет (Дата) -> нет (Валюта) -> нет (Поиск)
    mock_input.side_effect = ["2", "CANCELED", "нет", "нет", "нет"]

    # 3. Запускаем
    main()

    # 4. Проверяем, что в консоль вывелось количество операций
    # Ищем среди всех вызовов print строку,
    # содержащую "Всего банковских операций"
    printed_texts = [
        call.args[0] for call in mock_print.call_args_list if call.args
    ]
    assert any(
        "Всего банковских операций в выборке: 1" in text
        for text in printed_texts
    )


@patch("main.load_excel")
@patch("builtins.input")
@patch("builtins.print")
def test_main_full_scenario_excel(
    mock_print: Any, mock_input: Any, mock_get_excel: Any
) -> None:
    """
    Тестируем сценарий XLSX-файла
    """
    # 1. Мокаем XLSX-файл:
    mock_get_excel.return_value = [
        {
            "date": "2019-12-08T22:46:21.307722",
            "description": "Открытие вклада",
            "state": "CANCELED",
            "amount": "41096.24",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "to": "Счет 64686453677032553056",
        }
    ]

    # 2. Имитируем ответы пользователя:
    # 3 (XLSX) -> CANCELED (Статус) -> нет (Дата) -> нет (Валюта) -> нет (
    # Поиск)
    mock_input.side_effect = ["3", "CANCELED", "нет", "нет", "нет"]

    # 3. Запускаем
    main()

    # 4. Проверяем, что в консоль вывелось количество операций
    # Ищем среди всех вызовов print строку,
    # содержащую "Всего банковских операций"
    printed_texts = [
        call.args[0] for call in mock_print.call_args_list if call.args
    ]
    assert any(
        "Всего банковских операций в выборке: 1" in text
        for text in printed_texts
    )


@patch("main.get_transactions_from_json")
@patch("builtins.input")
@patch("builtins.print")
def test_main_no_results(
    mock_print: Any, mock_input: Any, mock_get_json: Any
) -> None:
    """
    Тестируем на пустой список
    """
    mock_get_json.return_value = []  # Файл пуст
    mock_input.side_effect = ["1", "EXECUTED", "нет", "нет", "нет"]

    main()

    printed_texts = [
        call.args[0] for call in mock_print.call_args_list if call.args
    ]
    assert any(
        "Не найдено ни одной операции" in text for text in printed_texts
    )
