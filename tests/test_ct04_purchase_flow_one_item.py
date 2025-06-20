import pytest
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.purchase
class TestPurchaseFlowOneItem:

    def test_purchase_single_item(self, driver):

        # --- ARRANGE ---

        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        cart_page = CartPage(driver)
        info_page = CheckoutInformationPage(driver)
        overview_page = CheckoutOverviewPage(driver)
        complete_page = CheckoutCompletePage(driver)

        # Test data
        product_name = "Sauce Labs Backpack"
        first_name = "Joao"
        last_name = "Silva"
        postal_code = "69310-048"

        # --- ACT ---

        # 1. Login
        login_page.perform_login("standard_user", "secret_sauce")
        home_page.verify_successful_login()

        # 2. Add product to cart
        home_page.add_item_to_cart(product_name)

        # 3. Go to cart and verify product
        home_page.go_to_cart()
        cart_page.verify_product_is_in_cart(product_name)

        # 4. Proceed through checkout
        cart_page.proceed_to_checkout()
        info_page.fill_information_and_continue(first_name, last_name, postal_code)
        overview_page.finish_checkout()

        # --- ASSERT ---

        # 1. Verify that the order confirmation page is displayed correctly
        complete_page.verify_order_completion()

        # 2. Return to the home page (final action)
        complete_page.return_to_home()

        # 3. Verify that the user is back on the home page
        home_page.verify_successful_login()