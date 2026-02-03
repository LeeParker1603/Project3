from typing import Dict, List


def filter_by_state(user_data_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Функция принимает список словарей и опционально значение ключа state (по умолчанию
    'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у
     которых ключ state соответствует указанному значению
    """

    new_user_data = []
    for data in user_data_list:
        if data.get("state") == state:
            new_user_data.append(data)
        else:
            continue

    return new_user_data


def sort_by_date(date_info_list: List[Dict], reverse_order: bool = True) -> List[Dict]:
    """
    Функция сортировки списка словарей по дате (по умолчанию - убывание)
    """

    sorted_list_dict = sorted(date_info_list, key=lambda x: x["date"], reverse=reverse_order)

    return sorted_list_dict
