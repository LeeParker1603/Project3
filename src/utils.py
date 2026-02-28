import json
import logging
import os
from typing import Any, Dict, List

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "logs/utils.log", mode="w", encoding="utf-8-sig"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Принимает путь до JSON-файла и возвращает список словарей с данными.
    Если файл пустой, содержит не список или не найден,
    возвращает пустой список.
    """
    if not os.path.exists(file_path):
        logger.error(f"Файл {file_path} не существует")
        return []

    try:
        logger.debug("Файл открывается для записи")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.debug("Проверяется, что данные — это список")
            if isinstance(data, list):
                logger.info(f"Получена транзакция из файла {file_path}")
                return data
            else:
                return []
    except FileNotFoundError:  # Ошибка файл не найден
        logger.error(f"Файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        # Ошибка декодирования или некорректные данные
        logger.error("Ошибка декодирования или некорректные данные")
        return []
