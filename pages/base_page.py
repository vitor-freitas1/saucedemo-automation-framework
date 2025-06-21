from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def type_in(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def is_element_displayed(self, locator):
        assert self.find_element(locator).is_displayed(), f"The element '{locator}' was not found on the screen."

    def get_element_text(self, locator):
        self.wait_for_element(locator)
        return self.find_element(locator).text

    def wait_for_element(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def verify_element_exists(self, locator):
        elements = self.find_elements(locator)
        assert len(elements) > 0, f"Element '{locator}' does not exist, but it was expected to not exist"

    def verify_element_does_not_exist(self, locator):
            assert len(self.find_elements(locator)) == 0, f"Element '{locator}' exists, but was not expected."

    def double_click(self, locator):
        element = self.wait_for_element(locator)
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator):
        element = self.wait_for_element(locator)
        ActionChains(self.driver).context_click(element).perform()

    def press_key(self, locator, key):
        element = self.find_element(locator)
        if key == "ENTER":
            element.send_keys(Keys.ENTER)
        elif key == "SPACE":
            element.send_keys(Keys.SPACE)
        elif key == "F1":
            element.send_keys(Keys.F1)