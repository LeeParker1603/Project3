from json import JSONDecodeError
from typing import Any
from unittest.mock import MagicMock, patch

import requests

from src.external_api import currency_conversion


# 1. Тест на RUB без сетевых запросов
def test_currency_conversion_rub(rub_transaction: Any) -> None:
    assert currency_conversion(rub_transaction) == 100.50


# 2. Тест на USD (успешный запрос через Mock)
@patch("requests.get")
@patch("os.getenv")
def test_currency_conversion_usd_success(
    mock_getenv: Any, mock_get: Any, usd_transaction: Any
) -> None:
    # Настраиваем фейковый API ключ
    mock_getenv.return_value = "fake_key"

    # Настраиваем фейковый ответ сервера
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 750.256}
    mock_get.return_value = mock_response

    result = currency_conversion(usd_transaction)

    # Проверяем округление и логику
    assert result == 750.26
    mock_get.assert_called_once()  # Проверяем, что запрос вообще был сделан


# 3. Тест на ошибку JSONDecodeError
@patch("requests.get")
@patch("os.getenv")
def test_currency_conversion_json_error(
    mock_getenv: Any, mock_get: Any, usd_transaction: Any, capsys: Any
) -> None:
    mock_getenv.return_value = "fake_key"

    mock_response = MagicMock()
    # Имитируем ошибку декодирования
    mock_response.json.side_effect = JSONDecodeError("Error", "doc", 0)
    mock_get.return_value = mock_response

    result = currency_conversion(usd_transaction)

    # Проверяем, что функция вернула None и вывела ошибку в консоль
    captured = capsys.readouterr()
    assert "Ошибка: Сервер прислал не JSON." in captured.out
    assert result is None


# 4. Тест на ошибку HTTP (например, 401 Unauthorized)
@patch("requests.get")
@patch("os.getenv")
def test_currency_conversion_http_error(
    mock_getenv: Any, mock_get: Any, usd_transaction: Any, capsys: Any
) -> None:
    # 1. Настройка окружения
    mock_getenv.return_value = "wrong_key"

    # 2. Создаем мок ответа
    mock_response = MagicMock()

    # Имитируем исключение.
    mock_get.side_effect = requests.exceptions.HTTPError("401 Client Error")
    mock_get.return_value = mock_response

    # 3. Вызов функции
    result = currency_conversion(usd_transaction)

    # 4. Проверки (Assertions)
    # Проверяем, что функция не упала, а вернула None
    # (так как в блоке except нет return)
    assert result is None

    # Проверяем, что в консоль напечаталось сообщение об ошибке
    captured = capsys.readouterr()
    assert "Ошибка HTTP: 401 Client Error" in captured.out
