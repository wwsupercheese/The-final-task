import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', 
                     action='store', 
                     default='en', 
                     help="Choose browser language")

@pytest.fixture(scope="function")
def browser(request):
    # Get browser language from command line
    browser_language = request.config.getoption('language')

    # Init option for chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})

    # Start browser for test
    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()