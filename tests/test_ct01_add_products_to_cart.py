import pytest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.cart
class Test01AddProductsToCart:
    def test_add_multiple_items_to_cart(self, driver):

        # --- ARRANGE ---
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        cart_page = CartPage(driver)

        # Product Data
        product_01_name = "Sauce Labs Backpack"
        product_02_name = "Sauce Labs Fleece Jacket"

        # --- ACT ---

        # Perform Login
        login_page.perform_login("standard_user", "secret_sauce")

        # Add the first item to the cart
        home_page.add_item_to_cart(product_01_name)

        # Go to the cart and verify the first item
        home_page.go_to_cart()
        cart_page.verify_product_is_in_cart(product_01_name)

        # Go back to the products page
        cart_page.click_continue_shopping()

        # Add the second item to the cart
        home_page.add_item_to_cart(product_02_name)

        # --- ASSERT ---

        # Go to the cart and verify both items are present
        home_page.go_to_cart()
        cart_page.verify_product_is_in_cart(product_01_name)
        cart_page.verify_product_is_in_cart(product_02_name)

        print("Test passed: Both items were successfully added to the cart.")
