import pytest

@pytest.mark.usefixtures("dataload")
class loaddata:
    def test_dataload1(self,dataload):
        print(dataload)
        print(dataload[0])
