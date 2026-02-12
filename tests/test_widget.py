import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "dates_info, date_output",
    zip(
        [
            "2024-03-11T02:26:18.671407",
            "2025-08-03D202:28:18.671408",
            "2025-09-30dT02:26:18.6714019",
            "2024-01-31fff02:26:18.671403377",
            "2024-",
            "2024-035-11T02:26:18.671407",
        ],
        [
            "11.03.2024",
            "03.08.2025",
            "30.09.2025",
            "31.01.2024",
            "Поле не может быть пустым или формат "
            "строки ХХХХ-ХХ-ХХ**************",
            "Формат строки обязательно: "
            "ХХХХ-ХХ-ХХ**************",
        ],
    ),
)
def test_get_date_correct(dates_info: str, date_output: str) -> None:
    assert get_date(dates_info) == date_output


def test_get_date_empty(empty: str) -> None:
    assert (
        get_date(empty)
        == "Поле не может быть пустым или формат "
           "строки ХХХХ-ХХ-ХХ**************"
    )


@pytest.mark.parametrize(
    "info_str, output_str",
    zip(
        [
            "Visa Platinum 7000792289606361",
            "Maestro 1596837868705199",
            "Счет 73654108430135874305",
        ],
        [
            "Visa Platinum 7000 79** **** 6361",
            "Maestro 1596 83** **** 5199",
            "Счет **4305",
        ],
    ),
)
def test_mask_account_card_correct(info_str: str, output_str: str) -> None:
    assert mask_account_card(info_str) == output_str


def test_mask_account_card_empty(empty: str) -> None:
    assert mask_account_card(empty) == "Введите тип и номер карты или счета"
