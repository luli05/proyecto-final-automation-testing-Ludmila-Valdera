import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.data_loader import load_data

pytestmark = pytest.mark.ui
DATA = load_data()

@pytest.fixture
def checkout(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.add_product(DATA["product"])
    inventory.open_cart()
    CartPage(logged_in).checkout()
    return CheckoutPage(logged_in)

def test_complete_purchase(checkout):
    checkout.enter_information(**DATA["checkout"])
    checkout.continue_checkout()
    assert DATA["product"] in checkout.products()
    checkout.finish()
    assert checkout.confirmation() == "Thank you for your order!"

def test_checkout_missing_fields(checkout):
    checkout.continue_checkout()
    assert "First Name is required" in checkout.error()
