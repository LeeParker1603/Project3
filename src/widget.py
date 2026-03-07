from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_str: str) -> str:
    """
    Принимает на вход строку, содержащую тип и номер карты или счета,
    и возвращает строку с замаскированным номером в зависимости от типа
    """
    if not isinstance(info_str, str):
        return "Счет не указан"
    if info_str != "":
        info_split = info_str.split()
        number = info_split[-1]
        name = " ".join(info_split[:-1])

        if name.lower() == "счет":
            return f"{name} {get_mask_account(number)}"
        else:
            return f"{name} {get_mask_card_number(number)}"
    else:
        return "Введите тип и номер карты или счета"


def get_date(date_info: str) -> str:
    """
    Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    if not isinstance(date_info, str):
        return "Дата не указана"

    if date_info != "" and len(date_info) > 8:
        if date_info[4] == "-" and date_info[7] == "-":
            date_info_split = date_info.split("-")
            year = date_info_split[0]
            month = date_info_split[1]
            day = date_info_split[2][:2]
        else:
            return "Формат строки обязательно: ХХХХ-ХХ-ХХ**************"

        return f"{day}.{month}.{year}"
    else:
        return (
            "Поле не может быть пустым или формат "
            "строки ХХХХ-ХХ-ХХ**************"
        )
