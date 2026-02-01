from src.masks import get_mask_card_number,get_mask_account

def mask_account_card(info_str: str) -> str:
    """
    Принимает на вход строку, содержащую тип и номер карты или счета,
    и возвращает строку с замаскированным номером в зависимости от типа
    """

    info_split = info_str.split()
    number = info_split[-1]
    name = " ".join(info_split[:-1])

    if name.lower() == "счет":
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_info: str) -> str:
    date_info_split = date_info.split("-")
    year = date_info_split[0]
    month = date_info_split[1]
    day = date_info_split[2][:2]

    return f"{day}.{month}.{year}"