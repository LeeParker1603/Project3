import json
import os
from typing import Any, Dict, List


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Принимает путь до JSON-файла и возвращает список словарей с данными.
    Если файл пустой, содержит не список или не найден,
    возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Проверяем, что данные — это список
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError, ValueError:
        # Ошибка декодирования или некорректные данные
        return []
