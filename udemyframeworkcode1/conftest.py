from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
# @pytest.fixture()
# def browsers(request):
#     service_obj = Service("D:\drivers\chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj)
#     driver.maximize_window()
#     driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
#     request.cls.driver = driver
#     yield driver
#     driver.quit()
import time
import pytest
driver=None # its screenshot purpose takes this
# its for browser invoke
def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default='chrome'
    )

@pytest.fixture(scope="class")
def browsers(request):
    global driver
    browsername=request.config.getoption("--browser_name")
    if browsername=="chrome":
        service_obj = Service("D:\drivers\chromedriver.exe")
        driver=webdriver.Chrome(service=service_obj)
    elif browsername=="firefox":
        service_obj = Service("D:\drivers\geckodriver.exe")
        driver=webdriver.firefox(service=service_obj)
    elif browsername=="edge":
        service_obj = Service("D:\drivers\msedgedriver.exe")
        driver=webdriver.Edge(service=service_obj)

        # cht = webdriver.ChromeOptions()
        # cht.add_argument("--disable-notifications")

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver # its apply the driver path class drivers
    yield
    driver.close()


@pytest.mark.hookwrapper
    #screenshot it takes when the test is failed
def pytest_runtest_makereport(item):
        """ Extends pytest.mark's hook to take and embed screenshot in html report, whenever test fails.
         :param item:
         """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])
        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
