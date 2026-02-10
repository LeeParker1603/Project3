from typing import List

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_numbers, masked_card",
    zip(
        [
            "7000792289606361",
            "6361700079228960",
            "7000896063617922",
            "6361792289607000",
        ],
        [
            "7000 79** **** 6361",
            "6361 70** **** 8960",
            "7000 89** **** 7922",
            "6361 79** **** 7000",
        ],
    ),
)
def test_get_mask_card_number(card_numbers: str, masked_card: str) -> None:
    assert get_mask_card_number(card_numbers) == masked_card


def test_get_mask_card_number_empty(empty: str) -> None:
    assert get_mask_card_number(empty) == "Необходимо ввести номер карты"


@pytest.mark.parametrize(
    "card_numbers", ["dddddddddddddddd", "aaaaaa6548888488", "ф", "sssdf"]
)
def test_get_mask_card_number_zero(card_numbers: str) -> None:
    assert (
        get_mask_card_number(card_numbers)
        == "Номер должен содержать только цифры"
    )


def test_get_mask_card_number_conform(list_numbers_non_conform: List) -> None:
    for numbers in list_numbers_non_conform:
        with pytest.raises(
            ValueError, match="Номер карты должен содержать 16 цифр."
        ):
            get_mask_card_number(numbers)


@pytest.mark.parametrize(
    "account_numbers, masked_account",
    zip(
        [
            "70007922896063616767",
            "63617000792289605733",
            "70008960636179222247",
            "63617922896070000001",
        ],
        ["**6767", "**5733", "**2247", "**0001"],
    ),
)
def test_get_mask_account_number(account_numbers: str,
                                 masked_account: str) -> None:
    assert get_mask_account(account_numbers) == masked_account


def test_get_mask_account_number_empty(empty: str) -> None:
    assert get_mask_account(empty) == "Необходимо ввести номер счета"


@pytest.mark.parametrize(
    "account_numbers",
    ["dddsddddddddddddd", "aasaaaa6548888488", "фs", "ssфsdf"],
)
def test_get_mask_account_number_zero(account_numbers: str) -> None:
    assert (
        get_mask_account(account_numbers)
        == "Номер должен содержать только цифры"
    )


def test_get_mask_account_conform(list_numbers_non_conform: List) -> None:
    for numbers in list_numbers_non_conform:
        with pytest.raises(
            ValueError, match="Номер счета должен содержать 20 цифр."
        ):
            get_mask_account(numbers)
