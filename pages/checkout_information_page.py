from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutInformationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def fill_information_and_continue(self, first_name, last_name, postal_code):
        self.type_in(self.first_name_field, first_name)
        self.type_in(self.last_name_field, last_name)
        self.type_in(self.postal_code_field, postal_code)
        self.click(self.continue_button)
