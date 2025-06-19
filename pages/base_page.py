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
        return self.find_element(locator).text