import pytest

from conftest import PASSWORD, STANDARD_USER
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_valid_login_opens_inventory(driver):
    LoginPage(driver).open().login(STANDARD_USER, PASSWORD)
    assert InventoryPage(driver).is_loaded()


@pytest.mark.parametrize("username, password, expected_error", [
    ("wrong_user", "wrong_pass", "Username and password do not match"),
    ("locked_out_user", PASSWORD, "Sorry, this user has been locked out"),
    ("", PASSWORD, "Username is required"),
    (STANDARD_USER, "", "Password is required"),
], ids=["invalid-credentials", "locked-out-user", "empty-username", "empty-password"])
def test_login_errors(driver, username, password, expected_error):
    page = LoginPage(driver).open()
    page.login(username, password)
    assert expected_error in page.error_message()
