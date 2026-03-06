from typing import Any

from src.data_loader import load_csv, load_excel
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import get_transactions_from_json
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Основная функция программы
    """

    print(
        "Привет! Добро пожаловать в программу работы\n"
        "с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    data: list[dict[Any, Any]] = []

    # 1. Запрашиваем источник данных
    while True:
        user_input_1: Any = input("\nВведите вариант (1, 2 или 3):\n")

        if user_input_1 not in ["1", "2", "3"]:
            print("\nОшибка! Пожалуйста, введите только 1, 2 или 3.")
            continue
        user_input_1 = int(user_input_1)
        if user_input_1 == 1:
            json_file = "data/operations.json"
            data = get_transactions_from_json(json_file)
            print("Для обработки выбран JSON-файл.")
            break
        elif user_input_1 == 2:
            csv_file = "data/transactions.csv"
            data = load_csv(csv_file)
            print("Для обработки выбран CSV-файл.")
            # print(data[-2:])
            break
        elif user_input_1 == 3:
            excel_file = "data/transactions_excel.xlsx"
            data = load_excel(excel_file)
            data = [{str(k): v for k, v in op.items()} for op in data]
            print("Для обработки выбран XLSX-файл.")
            # print(data[:2])
            break

    # 2. Фильтруем по статусу операции.
    status_list = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print(
            "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: {status_list[0]}, "
            f"{status_list[1]}, "
            f"{status_list[2]}"
        )
        user_input_2 = input()
        if not user_input_2.upper() in status_list:
            print(f'Статус операции "{user_input_2}" недоступен.')
            continue
        data = filter_by_state(data, user_input_2.upper())
        print(f'Операции отфильтрованы по статусу "{user_input_2.upper()}"')
        break

    # 3. Сортировка по дате
    while True:
        user_sort = input("Отсортировать операции по дате? Да/Нет: \n").lower()
        if user_sort not in ["да", "нет"]:
            continue

        if user_sort == "да":
            while True:
                order = input(
                    "Отсортировать по возрастанию" " или по убыванию? \n"
                ).lower()
                if order not in ["по убыванию", "по возрастанию"]:
                    continue

                is_reverse = True if order == "по убыванию" else False
                data = sort_by_date(data, is_reverse)
                break
            break
        break

    # 4. Фильтрация по валюте
    while True:
        user_currency = input(
            "Выводить только рублевые транзакции? Да/Нет: \n"
        ).lower()
        if user_currency not in ["да", "нет"]:
            continue

        if user_currency == "да":
            # Оставляем только те транзакции, где валюта — рубль
            data = [
                op
                for op in data
                if (
                    op.get("operationAmount", {})
                    .get("currency", {})
                    .get("code")
                    == "RUB"
                    or op.get("currency_code") == "RUB"
                )
            ]
            break
        break

    # 5. Фильтрация по слову в описании
    while True:
        user_search = input(
            "Отфильтровать список транзакций по определенному слову в "
            "описании? \n"
            "Да/Нет: "
        ).lower()
        if user_search not in ["да", "нет"]:
            continue
        if user_search == "да":
            search_word = input("Введите слово для поиска: \n")
            # Используем функцию process_bank_search с регулярными выражениями
            data = process_bank_search(data, search_word)
            break
        break

    # 6. Вывод результата
    print("\nРаспечатываю итоговый список транзакций...")
    if not data:
        print(
            "Не найдено ни одной операции, "
            "соответствующей выбранным критериям."
        )
    else:
        print(f"Всего банковских операций в выборке: {len(data)}\n")
        data = [op for op in data if op.get("date")]
        for op in data:
            date = get_date(op.get("date", "Неизвестно"))
            desc = op.get("description", "Без описания")
            to_account = mask_account_card(op.get("to", "Неизвестно"))
            if "from" not in op:
                # Если отправителя нет (например, открытие вклада)
                print(f"{date} {desc}")
                print(f"{to_account}")

            else:
                # Если отправитель есть (например, перевод)
                from_account = mask_account_card(op.get("from", ""))
                print(f"{date} {desc}")
                print(f"{from_account} -> {to_account}")

                # 3. Вывод суммы и валюты.
            if op.get("operationAmount"):
                amount = op.get("operationAmount", {}).get("amount")
                currency = (
                    op.get("operationAmount", {})
                    .get("currency", {})
                    .get("name")
                )
                print(f"Сумма: {amount} {currency}\n")
            elif not op.get("operationAmount"):
                amount = op.get("amount", {})
                currency = (
                    "руб."
                    if op.get("currency_code", {}) == "RUB"
                    else op.get("currency_code", {})
                )

                print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
