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

    # Проверяем, что функция вернула float и вывела ошибку в консоль
    captured = capsys.readouterr()
    assert "Ошибка: Сервер прислал не JSON." in captured.out
    assert result == 0.0


# 4. Тест на ошибку HTTP (например, 401 Unauthorized)
@patch("requests.get")
@patch("os.getenv")
def test_currency_conversion_http_error(
    usd_transaction: Any, capsys: Any
) -> None:
    with patch("requests.get") as mock_get:
        # Эмулируем исключение HTTPError
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = requests.HTTPError(
            "Simulated HTTP Error"
        )

        # Запускаем функцию и проверяем результат
        result = currency_conversion(usd_transaction)
        assert result == 0.0
