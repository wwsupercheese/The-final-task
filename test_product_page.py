import time

import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket (browser, link):
    # Arrange
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()

    # Act
    product_page.click_on_add_to_basket_btn()
    product_page.solve_quiz_and_get_code()

    # Assert
    product_page.should_be_add_to_basket()

@pytest.mark.basket
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
class TestBasketFromProductPage():
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        # Arrange
        main_page = ProductPage(browser=browser, url=link)
        main_page.open()

        # Act
        main_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)

        # Assert
        basket_page.should_not_be_content_in_basket()
        basket_page.should_be_content_title_is_empty()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        # Arrange
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()

        # Act
        product_page.click_on_add_to_basket_btn()
        product_page.solve_quiz_and_get_code()

        # Assert
        product_page.shoud_be_disappeared_succes_message()

    def test_guest_cant_see_success_message(self, browser, link):
        # Arrange
        product_page = ProductPage(browser=browser, url=link)

        # Act
        product_page.open()

        # Assert
        product_page.shoud_not_be_show_succes_message()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        # Arrange
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()

        # Act
        product_page.click_on_add_to_basket_btn()
        product_page.solve_quiz_and_get_code()

        # Assert
        product_page.shoud_not_be_show_succes_message()

@pytest.mark.login_guest
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
class TestLoginFromProductPage():
    @pytest.mark.need_review
    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        # Arrange
        product_page = ProductPage(browser=browser, url=link)

        # Act
        product_page.open()

        # Assert
        product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        # Arrange
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()

        # Act
        login_page = product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_login_page()

@pytest.mark.user
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link):
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()

        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        user_email = str(time.time()) + '@gmail.com'
        user_password = 'test_user'
        login_page.register_new_user(user_email, user_password)
        
        product_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser, link):
        # Arrange
        product_page = ProductPage(browser=browser, url=link)

        # Act
        product_page.open()

        # Assert
        product_page.shoud_not_be_show_succes_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        # Arrange
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()

        # Act
        product_page.click_on_add_to_basket_btn()

        # Assert
        product_page.should_be_add_to_basket()