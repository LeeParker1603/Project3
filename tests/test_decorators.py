from typing import Any

from src.decorators import log


@log(filename=None)
def log_testing(x: int, y: int) -> Any:
    return x / y


def test_log(capsys: Any) -> None:
    log_testing(10, 2)
    captured = capsys.readouterr()

    lines = captured.out.strip().split("\n")
    last_line = lines[-1]

    assert last_line == "log_testing ok"


def test_log_raises(capsys: Any) -> None:
    log_testing(10, 0)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "log_testing error: division by zero. Inputs (10, 0), {}\n"
    )


def test_log_save_to_file(tmp_path: Any) -> None:
    log_file = tmp_path / "test.log"

    @log(log_file)
    def log_testing_write(x: int, y: int) -> Any:
        return x / y

    log_testing_write(10, 0)

    last_line = ""
    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if lines:
            last_line = lines[-1]
    assert (
        last_line
        == "log_testing_write error: division by zero. Inputs (10, 0), {}\n"
    )
