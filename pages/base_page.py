from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def texts(self, locator):
        return [e.text for e in self.driver.find_elements(*locator)]

    def test_id(self, value):
        return (By.CSS_SELECTOR, f'[data-test="{value}"]')
