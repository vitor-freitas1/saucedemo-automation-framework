from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.cart_item = (By.XPATH, "//*[contains(text(), '{}')]")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.checkout_button = (By.ID, "checkout")

    def verify_product_is_in_cart(self, item_name):
        item_locator = (self.cart_item[0], self.cart_item[1].format(item_name))
        self.is_element_displayed(item_locator)

    def click_continue_shopping(self):
        self.click(self.continue_shopping_button)

    def proceed_to_checkout(self):
        self.click(self.checkout_button)
