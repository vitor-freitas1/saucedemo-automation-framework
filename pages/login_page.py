from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message_locator = (By.XPATH, "//*[@data-test='error']")

    def perform_login(self, username, password):
        self.type_in(self.username_field, username)
        self.type_in(self.password_field, password)
        self.click(self.login_button)

    def verify_error_message_is_displayed(self):
        self.is_element_displayed(self.error_message_locator)

    def verify_error_message_text(self, expected_text):
        found_text = self.get_element_text(self.error_message_locator)
        assert found_text == expected_text, f"The text found was '{found_text}', but the expected text was '{expected_text}'."