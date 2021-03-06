from commons.constants import Url
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = Url.PRODUCT_PAGE

    def add_product_to_basket(self):
        print("Adding product to basket")
        self.find_element(ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        print("Getting product name")
        product_name = self.find_element(ProductPageLocators.PRODUCT_NAME).text
        print(f"Product name is {product_name}")
        return product_name

    def get_product_price(self):
        print("Getting product price")
        product_price = self.find_element(ProductPageLocators.PRODUCT_PRICE).text
        print(f"Product price is {product_price}")
        return product_price

    def product_success_message_should_have(self, product_name):
        print(f"Checking that {product_name} is displayed in success message")
        assert product_name in self.find_element(ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE).text,\
            "Product name is not displayed in success message"

    def basket_total_should_be_equal(self, product_price):
        print(f"Checking that basket total equals {product_price}")
        assert product_price in self.find_element(ProductPageLocators.BASKET_TOTAL_MESSAGE).text,\
            "Basket total does not not equal to product price"

    def should_not_display_success_message(self):
        print("Checking that success message is not displayed")
        assert self.element_is_not_present(ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE),\
            "Success message is displayed, but should not be"

    def success_message_should_disappear(self):
        print("Checking that success message is disappeared after being displayed")
        assert self.element_is_disappeared(ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE),\
            "Success message is not disappeared"
