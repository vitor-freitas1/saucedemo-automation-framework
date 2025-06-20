from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.pony_express_image = (By.XPATH, "//img[@alt='Pony Express']")
        self.thank_you_header = (By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
        self.order_dispatched_message = (By.XPATH, "//*[contains(text(), 'Your order has been dispatched')]")
        self.back_home_button = (By.ID, "back-to-products")

    def verify_order_completion(self):
        self.is_element_displayed(self.pony_express_image)
        self.is_element_displayed(self.thank_you_header)
        self.is_element_displayed(self.order_dispatched_message)

    def return_to_home(self):
        self.click(self.back_home_button)

