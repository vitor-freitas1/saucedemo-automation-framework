import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():

    # setup
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # Automatically downloads and uses the correct chromedriver
    service = ChromeService(ChromeDriverManager().install())

    # The local variable for the browser instance
    browser = webdriver.Chrome(options=chrome_options)

    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get("https://www.saucedemo.com/")

    # --- Run Test ---
    # Yield the browser instance to the test function
    yield browser

    # --- Teardown ---
    # This will run after the test (or all tests in the session) is complete
    browser.quit()