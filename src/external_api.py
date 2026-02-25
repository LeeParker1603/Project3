import os
from json import JSONDecodeError
from typing import Any, Dict

import requests
from dotenv import load_dotenv


def currency_conversion(transaction: Dict) -> Any:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму
    транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount = transaction["operationAmount"]["amount"]
        return amount
    elif transaction["operationAmount"]["currency"]["code"] == "USD":
        try:
            currency_amount = transaction["operationAmount"]["amount"]
            url = "https://api.apilayer.com/exchangerates_data/convert"
            payload = {"amount": {currency_amount}, "from": "USD", "to": "RUB"}
            load_dotenv()
            apilayer_key = os.getenv("API_KEY")
            headers = {"apikey": f"{apilayer_key}"}
            response = requests.get(url, headers=headers, params=payload)
            conversion = response.json()
            amount = round(conversion["result"], 2)
            return amount
        except JSONDecodeError:
            print("Ошибка: Сервер прислал не JSON.")
        except requests.exceptions.HTTPError as err:
            print(f"Ошибка HTTP: {err}")
