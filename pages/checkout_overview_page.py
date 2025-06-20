from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Locator
        self.finish_button = (By.ID, "finish")

    def finish_checkout(self):
        self.click(self.finish_button)

