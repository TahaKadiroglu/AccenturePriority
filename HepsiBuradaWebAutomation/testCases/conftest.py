import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("--remote-allow-origins=*")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        print("Launching Chrome Browser")
    elif browser == 'edge':
        edge_options = Options()
        edge_options.add_argument("--remote-allow-origins=*")
        edge_options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):      #This will get the value from CLI/hook
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):               #This will return browser value to setup method
    return request.config.getoption("--browser")


#hook for adding environment info to report
def pytest_configure(config):
    config._metadata['Project Name'] = 'HepsiBuradaWebAutomation'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Taha'

#hook for delete modify environment info
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
