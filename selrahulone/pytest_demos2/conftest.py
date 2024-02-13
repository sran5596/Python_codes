import pytest

@pytest.fixture()
def setup():
    print("its first print")
    yield
    print("its last print")

@pytest.fixture(scope="class")
def dataload():
    print("data related")
    return ["sam","john","don"]

@pytest.fixture(params=["sam","john","don"])
def moredata(request):
    return request.param

@pytest.fixture(params=[("sam","rav","ndra"),("heo","done","hun"),("gt","ju","opi")])
def moredata2(request):
    return request.param