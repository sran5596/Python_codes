#same have the fixture below code first code example

# from selrahulone import *
# import pytest
#
# @pytest.fixture()
# def test_fixtures():
#     print("its first")
#     yield
#     print("its yeild last after test")
#
#
# def test_fixture_invoke(test_fixtures):
#     print("its actual test")


#conftest page have the fixtures below code is example
def test_invokefixture(setup):
    print("its actual test")