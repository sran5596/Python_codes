import pytest

@pytest.fixture
def setup1():
    print("setup")
    yield
    print("its last")

@pytest.fixture()
def dataload1():
    print("dataload")
    return [1,2,3]

@pytest.fixture(params=["r","g",6])
def moredata2(request):
    return request.param

@pytest.fixture(params=[(1,2,3),(4,5,6)])
def dataload2(request):
    return request.param