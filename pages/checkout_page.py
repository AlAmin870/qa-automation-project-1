from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")

    def start(self):
        self.click(self.CHECKOUT)

    def fill_details(self, first, last, postal):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE)

    def item_total(self):
        # Label reads "Item total: $29.99"
        return float(self.text_of(self.ITEM_TOTAL).split("$")[1])

    def finish(self):
        self.click(self.FINISH)

    def confirmation(self):
        return self.text_of(self.COMPLETE_HEADER)

    def error_message(self):
        return self.text_of(self.ERROR)
