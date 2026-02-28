import csv
from typing import Any, Dict, Hashable, List

import pandas as pd


def load_csv(file_csv: str) -> List[Dict[str, Any]]:
    """Функция считывает csv-файл, как список словарей"""
    with open(file_csv, mode="r", encoding="utf-8-sig") as file:
        # Указываем delimiter=';', так как в файле данные разделены ';'
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


def load_excel(file_excel: str) -> List[Dict[Hashable, Any]]:
    # engine='openpyxl' гарантирует использование нужной библиотеки
    df = pd.read_excel(file_excel, engine="openpyxl")
    dict_df = df.to_dict(orient="records")
    return dict_df
