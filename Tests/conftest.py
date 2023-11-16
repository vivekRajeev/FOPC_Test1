import pytest
from selenium import webdriver
# driver = None
from selenium.common.exceptions import WebDriverException

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    # driver = webdriver.Chrome()
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("headless")
    chrome_path = "C:/Users/windows/PycharmProjects/Makes_Excel_Validation/Utility/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.get('https://jakesweeneyag.fixedopspc.com')
    # driver.get("https://gossdodgechryslerramjeep.fixedopspc.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    # driver.close()



# @pytest.fixture()
# def admin_credential():
#     return [{"admin_username": "vivek.nair@citrusinformatics.com"}, {"admin_pwd": "fixedopsv1@123"}]
 # driver.get('https://sampackag-simt.fixedops.cc/auth/login')
        # driver.get('https://kunescountryag-simt.fixedops.cc')
    # driver.get('https://loveag-simt.fixedops.cc/auth/login')
    # driver.get('http://stiversag-simt.fixedops.cc/auth/login')
    # driver.get('https://kunescountryag.fixedopspc.com')
    # driver.get('https://sampackag.fixedopspc.com')

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("headless")
# chrome_path = "D:/pychrome/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_path,options=chrome_options)
# driver.get('https://sawyermotors-simt.fixedops.cc/auth/login')
# driver.implicitly_wait(9)
# request.cls.driver = driver
# yield
# driver.close()

# global driver