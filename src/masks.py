import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "logs/masks.log", mode="w", encoding="utf-8-sig"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты в виде числа и возвращает
    маску номера по правилу XXXX XX** **** XXXX"""
    logger.debug("Проверяется номер карты на пустое значение")
    if card_number != "":
        logger.debug("Проверяется номер карты, что введены цифры")
        if card_number.isdigit():
            card_str = str(card_number)

            logger.debug("Проверяется номер счета на количество символов")
            if len(card_str) != 16:
                logger.error(f"Введено {len(card_str)}. Должно быть 16")
                raise ValueError("Номер карты должен содержать 16 цифр.")
            logger.info("Замаскирован номер карты")
            formatted_number_card = (
                f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
            )
            return formatted_number_card
        else:
            logger.error("Введены буквенные значения")
            return "Номер должен содержать только цифры"
    else:
        logger.error("Не введено никаких символов")
        return "Необходимо ввести номер карты"


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX,
    где X — это цифра номера
    """
    logger.debug("Проверяется номер счета на пустое значение")
    if account_number != "":
        logger.debug("Проверяется номер счета, что введены цифры")
        if account_number.isdigit():
            account_str = str(account_number)

            logger.debug("Проверяется номер счета на количество символов")
            if len(account_str) != 20:
                logger.error(f"Введено {len(account_str)}. Должно быть 20")
                raise ValueError("Номер счета должен содержать 20 цифр.")
            logger.info("Замаскирован номер счета")
            formatted_account_number = f"**{account_str[-4:]}"
            return formatted_account_number
        else:
            logger.error("Введены буквенные значения")
            return "Номер должен содержать только цифры"
    else:
        logger.error("Не введено никаких символов")
        return "Необходимо ввести номер счета"
