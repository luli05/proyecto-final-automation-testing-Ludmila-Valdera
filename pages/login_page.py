from pages.base_page import BasePage

class LoginPage(BasePage):
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.fill(self.test_id("username"), username)
        self.fill(self.test_id("password"), password)
        self.click(self.test_id("login-button"))

    def error(self):
        return self.text(self.test_id("error"))

    def is_visible(self):
        return self.wait.until(lambda d: d.find_element(*self.test_id("login-button")).is_displayed())
