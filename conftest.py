from datetime import datetime
from pathlib import Path
import re
import pytest
import pytest_html
from selenium import webdriver
from pages.login_page import LoginPage
from utils.data_loader import load_data

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1440,1000")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture
def logged_in(driver):
    page = LoginPage(driver)
    page.open()
    page.login(**load_data()["login"])
    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    browser = item.funcargs.get("driver")
    if report.failed and report.when in ("setup", "call") and browser is not None:
        try:
            folder = Path("reports/screenshots")
            folder.mkdir(parents=True, exist_ok=True)
            name = re.sub(r"[^a-zA-Z0-9_-]", "_", item.nodeid)
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            path = folder / f"{name}_{stamp}.png"
            browser.save_screenshot(str(path))
            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(browser.get_screenshot_as_base64()))
            report.extras = extras
        except Exception as exc:
            report.sections.append(("Screenshot", str(exc)))
