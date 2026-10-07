BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"


def test_add_single_item_updates_badge(logged_in):
    logged_in.add_to_cart(BACKPACK)
    assert logged_in.cart_count() == 1


def test_add_multiple_items(logged_in):
    logged_in.add_to_cart(BACKPACK)
    logged_in.add_to_cart(BIKE_LIGHT)
    assert logged_in.cart_count() == 2


def test_remove_item_clears_badge(logged_in):
    logged_in.add_to_cart(BACKPACK)
    logged_in.remove_from_cart(BACKPACK)
    assert logged_in.cart_count() == 0


def test_sort_price_low_to_high(logged_in):
    logged_in.sort_by("lohi")
    prices = logged_in.prices()
    assert prices == sorted(prices)
