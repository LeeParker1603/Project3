import pytest

@pytest.fixture
def empty():
    return ''


@pytest.fixture(params=['5465464', '0', '58882425499887787878789988798', '368'])
def list_numbers_non_conform(request):
    return request.param