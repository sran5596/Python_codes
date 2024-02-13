import pytest

@pytest.mark.usefixtures("setup")
@pytest.mark.smoke
def test_demo1():
    print("its actual test")
