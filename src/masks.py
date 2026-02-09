def get_mask_card_number(card_number: int | str) -> str:
    """Принимает на вход номер карты в виде числа и возвращает
    маску номера по правилу XXXX XX** **** XXXX"""
    if card_number != '':
        if card_number.isdigit():
            card_str = str(card_number)

            if len(card_str) != 16:
                raise ValueError("Номер карты должен содержать 16 цифр.")
            formatted_number_card = (
                f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
            )
            return formatted_number_card
        else:
            return "Номер должен содержать только цифры"
    else:
        return "Необходимо ввести номер карты"


def get_mask_account(account_number: int | str) -> str:
    """Принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX,
    где X — это цифра номера
    """
    if account_number != '':
        if account_number.isdigit():
            account_str = str(account_number)

            if len(account_str) != 20:
                raise ValueError("Номер счета должен содержать 20 цифр.")
            formatted_account_number = f"**{account_str[-4:]}"
            return formatted_account_number
        else:
            return "Номер должен содержать только цифры"
    else:
        return "Необходимо ввести номер счета"
