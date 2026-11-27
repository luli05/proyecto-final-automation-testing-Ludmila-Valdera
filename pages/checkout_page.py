from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def enter_information(self, first_name, last_name, postal_code):
        self.fill(self.test_id("firstName"), first_name)
        self.fill(self.test_id("lastName"), last_name)
        self.fill(self.test_id("postalCode"), postal_code)

    def continue_checkout(self):
        self.click(self.test_id("continue"))

    def products(self):
        return self.texts(self.test_id("inventory-item-name"))

    def finish(self):
        self.click(self.test_id("finish"))

    def confirmation(self):
        return self.text(self.test_id("complete-header"))

    def error(self):
        return self.text(self.test_id("error"))
