import pytest
from selrahulone.pytest_demos2.BaseClass_logging_code_py import Baseclass_logging

@pytest.mark.usefixtures("moredata ")
class import_logging(Baseclass_logging):
    def test_moredata3(self,moredata):
        log=self.test_loggingDemo()
        log.info(moredata[0])