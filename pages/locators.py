from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout_link")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_TITLE = (By.CSS_SELECTOR, ".page-header h1")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name='login_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_ADDED_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-of-type(1) .alertinner")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner p:nth-of-type(1)")
