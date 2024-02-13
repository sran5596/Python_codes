import pytest
# its for  ficture execute
@pytest.fixture(scope='class')
def setup():
    print("its fixture first")
    yield
    print("its yield last")
#its for dataload to the test after that pass below method name to your test beside of self,dataload
@pytest.fixture(scope='class')
def dataload():
    print("its dataload first")
    return["Sampathi","Raveendra","Heroo"]
# its invoke the every browser and take one by one here
@pytest.fixture(params=["chrome","firefox","IE"]) #its pasing the single list
def browser(request): #request is responsible for take each element and pass to test
    return request.param # return the value

@pytest.fixture(params=[("sam","rav","ndra"),("heo","done","hun"),("gt","ju","opi")])
def moredata(request):
    return request.param