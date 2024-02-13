# import pytest
#
# # @pytest.mark.usefixtures("dataload")
# # class fixdataload:
# #     def test_dataloadtest1(self,dataload):
# #         print("its for first demo")
# #         print(dataload)
# wrapping with the class its not working above code

def test_dataload(dataload):
    print("its for first demo")
    print(dataload)