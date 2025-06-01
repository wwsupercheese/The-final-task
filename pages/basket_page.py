from selenium.webdriver.common.by import By

from .base_page import BasePage

from .locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_content_title_is_empty(self):
        basket_content = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT_INNER)
        basket_content_title = basket_content.find_element(*BasketPageLocators.BASKET_CONTENT_INNER_TITLE)
        assert 'Your basket is empty' in basket_content_title.text, "Basket don't have title"

    def should_not_be_content_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT_INNER_ITEMS), "Basket have items"