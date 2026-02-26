import os
from json import JSONDecodeError
from typing import Dict

import requests
from dotenv import load_dotenv


def currency_conversion(transaction: Dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму
    транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    """
    currency_code = transaction["operationAmount"]["currency"]["code"]
    raw_amount = transaction["operationAmount"]["amount"]

    # 1. Если это рубли, возвращаем сразу
    if currency_code == "RUB":
        return round(float(raw_amount), 2)

    # 2. Если это валюта, которую надо конвертировать
    if currency_code in ("USD", "EUR"):
        try:
            load_dotenv()
            apilayer_key = os.getenv("API_KEY")

            url = "https://api.apilayer.com/exchangerates_data/convert"
            payload = {
                "amount": raw_amount,
                "from": currency_code,
                "to": "RUB",
            }
            headers = {"apikey": f"{apilayer_key}"}

            response = requests.get(
                url, headers=headers, params=payload, timeout=10
            )

            # проверка на HTTPError
            response.raise_for_status()

            conversion = response.json()
            return round(float(conversion["result"]), 2)

        except (JSONDecodeError, requests.exceptions.RequestException):
            print("Ошибка: Сервер прислал не JSON.")
            return 0.0

    # 3. Финальный возврат для любой другой валюты
    return 0.0
