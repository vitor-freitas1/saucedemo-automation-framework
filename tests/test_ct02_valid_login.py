import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.login
class Test02ValidLogin:
    def test_valid_login(self, driver):

        # --- ARRANGE ---
        login_page = LoginPage(driver)
        home_page = HomePage(driver)

        # --- ACT ---

        # Perform login with valid credentials
        login_page.perform_login("standard_user", "secret_sauce")

        # --- ASSERT ---

        # Verify that the login was successful by checking for the products page title
        home_page.verify_successful_login()
