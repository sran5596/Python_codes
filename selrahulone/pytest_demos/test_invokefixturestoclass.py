import pytest

@pytest.mark.usefixtures("setup")

class invoke:

    def test_invokedemo1(self):
        print("its test one")

    def test_invokedemo2(self):
        print("its test second ")

    def test_invokedemo3(self):
        print("its test third ")
