from playwright.sync_api import Page, expect
class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_dropdown = page.locator("[data-test=\"product-sort-container\"]")
        self.prices_locator = page.locator("[data-test=\"inventory-item-price\"]")
    def sort_products(self, sort_option: str):
        self.sort_dropdown.select_option(sort_option)
    def get_prices(self):
        return self.prices_locator.all_text_contents()