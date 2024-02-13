import pytest
from selrahulone.pytest_demos.BaseClass_logging_code import Baseclass_logging

@pytest.mark.usefixtures("setup1")
def test1_demo(setup1):
    print("test1")

def test_getdata(dataload1):
    print(dataload1[0])

def test_moredata(moredata2):
    print(moredata2)

def test_getdata2(dataload2):
    # log=Baseclass_logging.test_loggingDemo()
    # log.INFO(dataload2[0])
    print(dataload2[0])
    print(dataload2[1])
