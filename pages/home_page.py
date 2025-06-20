from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.inventory_item_name = (By.XPATH, "//*[contains(text(), '{}')]")
        self.add_to_cart_button = (By.XPATH, "//*[text()='Add to cart']")
        self.cart_icon = (By.XPATH, "//*[@class='shopping_cart_link']")

    def verify_successful_login(self):
        self.is_element_displayed(self.page_title)

    def add_item_to_cart(self, item_name):
        product_link_locator = (self.inventory_item_name[0], self.inventory_item_name[1].format(item_name))
        self.click(product_link_locator)
        self.click(self.add_to_cart_button)

    def go_to_cart(self):
        self.click(self.cart_icon)