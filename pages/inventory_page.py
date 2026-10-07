from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT = (By.CLASS_NAME, "product_sort_container")
    PRICES = (By.CLASS_NAME, "inventory_item_price")

    def is_loaded(self):
        self.wait.until(EC.url_contains("inventory"))
        return self.text_of(self.TITLE) == "Products"

    def add_to_cart(self, item_id):
        self.click((By.ID, f"add-to-cart-{item_id}"))

    def remove_from_cart(self, item_id):
        self.click((By.ID, f"remove-{item_id}"))

    def cart_count(self):
        if not self.is_present(self.CART_BADGE):
            return 0
        return int(self.text_of(self.CART_BADGE))

    def sort_by(self, value):
        Select(self.find(self.SORT)).select_by_value(value)

    def prices(self):
        return [float(e.text.replace("$", "")) for e in self.driver.find_elements(*self.PRICES)]

    def open_cart(self):
        self.click(self.CART_LINK)
