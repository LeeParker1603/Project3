from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.data_loader import load_csv, load_excel


@patch("builtins.open", new_callable=mock_open, read_data="id;amount\n1;100")
def test_load_csv(mock_file: Any) -> None:
    """Используем mock_file из декоратора patch"""
    result = load_csv("fake.csv")

    assert result == [{"id": "1", "amount": "100"}]
    mock_file.assert_called_once_with(
        "fake.csv", mode="r", encoding="utf-8-sig"
    )


@patch("builtins.open", side_effect=FileNotFoundError)
def test_load_csv_file_not_found(_: Any) -> None:
    """Проверка поведения при отсутствии файла"""

    with pytest.raises(FileNotFoundError):
        load_csv("non_existent.csv")


@patch("pandas.read_excel")  # Патчим всю функцию чтения пандас
def test_load_excel(mock_read: Any) -> None:
    # 1. Готовим фейковый DataFrame, который якобы вернул pandas
    mock_df = pd.DataFrame([{"id": "1", "amount": "100"}])
    mock_read.return_value = mock_df

    # 2. Вызываем функцию
    result = load_excel("fake.xlsx")

    # 3. Проверяем результат
    assert result == [{"id": "1", "amount": "100"}]

    # 4. Проверяем, что pandas вызвали с правильным путем
    mock_read.assert_called_once_with("fake.xlsx", engine="openpyxl")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_load_excel_file_not_found(_: Any) -> None:
    """Проверка поведения при отсутствии файла"""

    with pytest.raises(FileNotFoundError):
        load_csv("non_existent.xlsx")
