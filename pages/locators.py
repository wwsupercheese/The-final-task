from selenium.webdriver.common.by import By

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, 'btn-add-to-basket')

    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')

    ALERTTINNER_TITLE = (By.CSS_SELECTOR, '#messages > :nth-child(1) strong')
    ALERTTINNER_PRICE = (By.CSS_SELECTOR, '#messages > :nth-child(3) strong')

    SUCCES_MESSAGE = (By.CSS_SELECTOR, '#messages > :nth-child(1)')

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTER_FORM = (By.CLASS_NAME, "register_form")

    REGISTER_EMAIL_INPUT = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD_INPUT = (By.ID, 'id_registration-password1')
    REGISTER_CONFIRM_PASSWORD_INPUT = (By.ID, 'id_registration-password2')
    REGISTER_CONFIRM_BTN = (By.NAME, 'registration_submit')

class BasketPageLocators():
    BASKET_CONTENT_INNER = (By.ID, 'content_inner')
    BASKET_CONTENT_INNER_TITLE = (By.TAG_NAME, 'p')
    BASKET_CONTENT_INNER_ITEMS = (By.CLASS_NAME, 'basket-items')