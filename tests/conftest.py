import pytest
from typing import Any


@pytest.fixture
def empty() -> str:
    return ""


@pytest.fixture(
    params=["5465464", "0", "58882425499887787878789988798", "368"]
)
def list_numbers_non_conform(request: Any) -> Any:
    return request.param
