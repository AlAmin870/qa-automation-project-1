import os
from pathlib import Path

import pytest
from selenium import webdriver

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# Public demo credentials published on saucedemo.com
STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"
SCREENSHOT_DIR = Path("reports/screenshots")


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,768")
    # Stop Chrome's password-manager popups from blocking clicks after login
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    driver = webdriver.Chrome(options=options)  # Selenium Manager downloads the matching driver
    yield driver
    driver.quit()  # runs even when the test fails


@pytest.fixture
def logged_in(driver):
    LoginPage(driver).open().login(STANDARD_USER, PASSWORD)
    inventory = InventoryPage(driver)
    assert inventory.is_loaded()
    return inventory


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot whenever a test fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed and "driver" in item.fixturenames:
        SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
        item.funcargs["driver"].save_screenshot(str(SCREENSHOT_DIR / f"{item.name}.png"))
