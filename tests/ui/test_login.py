import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_data

pytestmark = pytest.mark.ui

def test_valid_login(logged_in):
    assert InventoryPage(logged_in).title() == "Products"

@pytest.mark.parametrize("case", load_data()["invalid_login"], ids=["wrong_password", "locked_user"])
def test_invalid_login(driver, case):
    page = LoginPage(driver)
    page.open()
    page.login(case["username"], case["password"])
    assert case["error"] in page.error()

def test_logout(logged_in):
    InventoryPage(logged_in).logout()
    assert LoginPage(logged_in).is_visible()
