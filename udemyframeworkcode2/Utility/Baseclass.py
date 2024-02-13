from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys
import pytest
import inspect
import logging
from udemyframeworkcode2.testdata.Testdata import testdata
@pytest.mark.usefixtures("setup","datalog")
class Baseclass:

    def waits(self,text):
        mywait=WebDriverWait(self.driver,10)
        mywait.until(EC.visibility_of_element_located((By.XPATH,text)))

    def selectofelement(self,locater,text):
        sel=Select(locater)
        sel.select_by_visible_text(text)

    def test_loggingDemo(self):
            loggername = inspect.stack()[1][3]
            # logger = logging.getLogger(__name__)  # here[__name__] give the testcase name
            logger = logging.getLogger(loggername)  # use this compare to above
            # below code inspect code gives the testcase name on result
            loggername = inspect.stack()[1][3]

            filehandler = logging.FileHandler(
                "logs.log")  # its identify the place of the testcases location their gives
            # below formatter about in logs its give strecture
            formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
            # below one display the output
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)  # its create the connection to filehandler(filehandler obj)
            logger.setLevel(logging.DEBUG)  # here pass the which one you need to pass here
            logger.info("its info details related")
            logger.warning("its shows the warning ")
            logger.error("its shows the error")
            logger.critical("its shows the critical")
            logger.debug("its show the debug related details")
            return logger

    def actionchains(self):
        action=ActionChains(self.driver)
        return action


