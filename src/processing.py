import re
from collections import Counter
from typing import Dict, List


def filter_by_state(
    user_data_list: List[Dict], state: str = "EXECUTED"
) -> List[Dict]:
    """
    Функция принимает список словарей и опционально значение ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует
    указанному значению
    """

    new_user_data = []
    for data in user_data_list:
        if data.get("state") == state:
            new_user_data.append(data)
        else:
            continue

    return new_user_data


def sort_by_date(
    date_info_list: List[Dict], reverse_order: bool = True
) -> List[Dict]:
    """
    Функция сортировки списка словарей по дате (по умолчанию - убывание)
    """

    sorted_list_dict = sorted(
        date_info_list,
        key=lambda x: str(x.get("date", "")),
        reverse=reverse_order,
    )

    return sorted_list_dict


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Фильтрует список словарей
    по наличию строки поиска в описании (description).
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    filtered_data = [
        op for op in data if pattern.search(str(op.get("description", "")))
    ]

    return filtered_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Считает количество операций для каждой категории из списка.
    Ключи — названия категорий, значения — количество найденных операций.
    """
    # Извлекаем все описания из операций, которые входят в наш список категорий
    descriptions = [
        op.get("description")
        for op in data
        if op.get("description") in categories
    ]

    # Counter создаст словарь с частотой каждого описания
    counts = Counter(descriptions)

    # Убеждаемся, что в итоговом словаре есть все категории из списка,
    # даже если они 0
    category_counts = {
        category: counts.get(category, 0) for category in categories
    }
    return category_counts
