import pytest

@pytest.mark.usefixtures("setup")
class invokefixture:
    def test_demo1(self):
        print("its for first demo")

    def test_demo2(self):
        print("its for second demo")

    def test_demo3(self):
        print("its for third demo")