import pytest
from pages.login_page import LoginPage


@pytest.mark.login
class Test03InvalidLogin:

    def test_invalid_login_with_wrong_password(self, driver):

        # --- ARRANGE ---
        login_page = LoginPage(driver)

        # Test data
        expected_error_message = "Epic sadface: Username and password do not match any user in this service"

        # --- ACT ---

        # Perform login with incorrect credentials
        login_page.perform_login("standard_user", "wrong_password")

        # --- ASSERT ---

        # Verify that the error message is displayed
        login_page.verify_error_message_is_displayed()

        # Verify the error message text
        login_page.verify_error_message_text(expected_error_message)