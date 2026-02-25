import json
from typing import Any

from src.utils import get_transactions_from_json


def test_get_transactions_valid_data(tmp_path: Any) -> None:
    """Проверка корректного чтения валидного JSON-списка."""
    data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    file = tmp_path / "test.json"
    file.write_text(json.dumps(data), encoding="utf-8")

    assert get_transactions_from_json(str(file)) == data


def test_get_transactions_not_a_list(tmp_path: Any) -> None:
    """Проверка случая, когда JSON содержит объект (словарь), а не список."""
    data = {"id": 1, "amount": 100}
    file = tmp_path / "test_dict.json"
    file.write_text(json.dumps(data), encoding="utf-8")

    assert get_transactions_from_json(str(file)) == []


def test_get_transactions_file_not_found() -> None:
    """Проверка поведения, если файл не существует."""
    assert get_transactions_from_json("non_existent_file.json") == []


def test_get_transactions_invalid_json(tmp_path: Any) -> None:
    """Проверка случая с битым JSON (синтаксическая ошибка)."""
    file = tmp_path / "invalid.json"
    file.write_text("{ 'bad_json': True ", encoding="utf-8")

    assert get_transactions_from_json(str(file)) == []


def test_get_transactions_empty_file(tmp_path: Any) -> None:
    """Проверка пустого файла."""
    file = tmp_path / "empty.json"
    file.write_text("", encoding="utf-8")

    assert get_transactions_from_json(str(file)) == []


def test_get_transactions_not_json_content(tmp_path: Any) -> None:
    """Проверка файла с произвольным текстом."""
    file = tmp_path / "text.txt"
    file.write_text("Hello world", encoding="utf-8")

    assert get_transactions_from_json(str(file)) == []
