from pages.base_page import BasePage

class CartPage(BasePage):
    def products(self):
        return self.texts(self.test_id("inventory-item-name"))

    def remove_product(self, name):
        self.click(self.test_id("remove-" + name.lower().replace(" ", "-")))

    def checkout(self):
        self.click(self.test_id("checkout"))
