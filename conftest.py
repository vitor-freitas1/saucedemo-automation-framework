import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", help="Run browser in headless mode"
    )


@pytest.fixture(scope="session")
def driver(request):

    # --- Setup ---
    chrome_options = Options()

    # In case 'pytest --headless' is used
    if request.config.getoption("headless"):
        chrome_options.add_argument("--headless")

    chrome_options.add_argument("--incognito")

    # Automatically downloads and uses the correct chromedriver
    service = ChromeService(ChromeDriverManager().install())

    # The local variable for the browser instance
    browser = webdriver.Chrome(service=service, options=chrome_options)

    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get("https://www.saucedemo.com/")

    # --- Run Test ---
    # Yield the browser instance to the test function
    yield browser

    # --- Teardown ---
    # This will run after the test (or all tests in the session) is complete
    browser.quit()