import pytest
from pages.inventory_page import InventoryPage

@pytest.mark.ui
def test_sort_prices(logged_in):
    page = InventoryPage(logged_in)
    page.sort_low_to_high()
    prices = page.prices()
    assert len(prices) > 1
    assert prices == sorted(prices)
