from pages.checkout_page import CheckoutPage

BACKPACK = "sauce-labs-backpack"
BACKPACK_PRICE = 29.99


def test_complete_checkout(driver, logged_in):
    logged_in.add_to_cart(BACKPACK)
    logged_in.open_cart()
    checkout = CheckoutPage(driver)
    checkout.start()
    checkout.fill_details("Test", "User", "1205")
    assert checkout.item_total() == BACKPACK_PRICE
    checkout.finish()
    assert checkout.confirmation() == "Thank you for your order!"


def test_checkout_requires_postal_code(driver, logged_in):
    logged_in.add_to_cart(BACKPACK)
    logged_in.open_cart()
    checkout = CheckoutPage(driver)
    checkout.start()
    checkout.fill_details("Test", "User", "")
    assert "Postal Code is required" in checkout.error_message()
