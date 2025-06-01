from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def click_on_add_to_basket_btn(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_add_to_basket(self):
        alertinner_title = self.browser.find_element(*ProductPageLocators.ALERTTINNER_TITLE)
        alertinner_price= self.browser.find_element(*ProductPageLocators.ALERTTINNER_PRICE)

        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)

        assert product_title.text == alertinner_title.text, "Message do not have product title"
        assert product_price.text == alertinner_price.text, "Message do not have product price"

    def shoud_be_disappeared_succes_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCES_MESSAGE), "Succes message is disappear on page"

    def shoud_not_be_show_succes_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_MESSAGE), "Succes message is showing on page"