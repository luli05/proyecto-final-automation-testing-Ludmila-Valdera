from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    def title(self):
        return self.text(self.test_id("title"))

    def add_product(self, name):
        self.click(self.test_id("add-to-cart-" + name.lower().replace(" ", "-")))

    def open_cart(self):
        self.click(self.test_id("shopping-cart-link"))

    def sort_low_to_high(self):
        Select(self.wait.until(EC.visibility_of_element_located(self.test_id("product-sort-container")))).select_by_value("lohi")

    def prices(self):
        return [float(v.replace("$", "")) for v in self.texts(self.test_id("inventory-item-price"))]

    def logout(self):
        from selenium.webdriver.common.by import By
        self.click((By.ID, "react-burger-menu-btn"))
        self.click(self.test_id("logout-sidebar-link"))
