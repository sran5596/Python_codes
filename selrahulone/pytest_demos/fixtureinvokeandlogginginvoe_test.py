import pytest
from selrahulone.pytest_demos.BaseClass_logging_code import Baseclass_logging
@pytest.mark.usefixtures("dataload")
class test_logandfixinvoke(Baseclass_logging):

    def test_dataload3(self,dataload):
        print("its for first demo")

        #accesssing the parent method below createred the objcet to as [log]
        log=self.test_loggingDemo()

        #below code for printing the data in info error show in their log file
        log.info(dataload[0])
        log.info(dataload[2])
        # result shows like 2023-11-03 16:32:01,259 :INFo :selrahuldemo.BaseClass: raveendra

