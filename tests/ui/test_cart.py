import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.data_loader import load_data

pytestmark = pytest.mark.ui
PRODUCT = load_data()["product"]

@pytest.fixture
def cart(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.add_product(PRODUCT)
    inventory.open_cart()
    return CartPage(logged_in)

def test_add_product(cart):
    assert PRODUCT in cart.products()

def test_remove_product(cart):
    assert PRODUCT in cart.products()
    cart.remove_product(PRODUCT)
    assert cart.products() == []
