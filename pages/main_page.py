from selenium.webdriver.common.by import By

from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)