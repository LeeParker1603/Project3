import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv


def currency_conversion(transaction: Dict) -> Any:
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount = transaction["operationAmount"]["amount"]
        return amount
    elif transaction["operationAmount"]["currency"]["code"] == "USD":
        currency_amount = transaction["operationAmount"]["amount"]
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {"amount": {currency_amount}, "from": "USD", "to": "RUB"}
        load_dotenv()
        apilayer_key = os.getenv("API_KEY")
        headers = {"apikey": f"{apilayer_key}"}
        response = requests.get(url, headers=headers, params=payload)
        conversion = response.json()
        # conversion = json.loads(convert_json, indent=4)
        amount = round(conversion["result"], 2)
        return amount
