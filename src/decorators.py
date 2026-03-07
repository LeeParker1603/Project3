import sys
from datetime import datetime
from functools import wraps
from time import time
from typing import Any


def log(filename: Any = None) -> Any:
    """
    Декоратор, который автоматически логирует начало
    и конец выполнения функции, а также ее результаты
    или возникшие ошибки.
    Декоратор должен принимать необязательный аргумент
    filename, который определяет, куда будут записываться логи
    (в файл или в консоль):
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль.
    """

    def log_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None
            start_time = datetime.fromtimestamp(time())
            try:
                result = func(*args, **kwargs)
                end_time = datetime.fromtimestamp(time())
                log_message = (
                    f"Время начала: {start_time}\n"
                    f"Время окончания: {end_time}\n"
                    f"{func.__name__} ok\n"
                )
            except Exception as e:
                log_message = (
                    f"{func.__name__} error: {e}. Inputs {args}, {kwargs}\n"
                )
            if filename:
                # Запись в файл
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(log_message)
            else:
                # Вывод в консоль
                sys.stdout.write(log_message)
            return result

        return wrapper

    return log_decorator
